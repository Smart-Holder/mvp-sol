
pragma solidity ^0.6.12;
pragma experimental ABIEncoderV2;

import './nft_proxy.sol';

contract ERC1155Proxy is IERC1155Receiver, NFTProxy {
	using Address for address;

	struct Balances {
		uint256 total; // tokenId total
		mapping (address => Owners) values; // map( owner => Owners )
	}
	// token => map( tokenId => Balances )
	mapping (address => mapping(uint256 => Balances)) internal _assets;

	bytes4 private constant _ERC1155_RECEIVED = 0xf23a6e61;
	bytes4 private constant _ERC1155_BATCH_RECEIVED = 0xbc197c81;
	bytes4 private constant _INTERFACE_ID_ERC1155 = 0xd9b67a26;

	function initialize() public {
		__NFTProxy_init();
		_registerInterface(
			ERC1155Proxy(address(0)).onERC1155Received.selector ^
			ERC1155Proxy(address(0)).onERC1155BatchReceived.selector
		);
	}

	// @dev convert addr to standard ERC1155 NFT,will be revered if add is invalid.
	function _isERC1155(address addr) internal view returns (IERC1155) {
		require(
			addr.isContract(),
			"#ERC1155Proxy#_isERC1155: INVLIAD_CONTRACT_ADDRESS"
		);
		require(
			IERC1155(addr).supportsInterface(_INTERFACE_ID_ERC1155),
			"The NFT contract has an invalid ERC1155 implementation"
		);
		return IERC1155(addr);
	}

	function _onERC1155Received(
		IERC1155 token, address from, address[] memory toOwners, uint256 id, uint256 value, uint256 signCount
	) private {
		Balances storage ba = _assets[address(token)][id];
		require(
			token.balanceOf(address(this), id) >= ba.total + value,
			"#ERC1155Proxy#_onERC1155Received: INVALID_AMOUNT"
		);
		Owners memory owners_ = checkOwners(address(token), id, toOwners, signCount);

		address to = toOwners[0];
		Owners storage owners = ba.values[to];
		uint256 toBalances = owners.balances + value;

		owners.balances = toBalances;
		owners.owners = owners_.owners;
		owners.signCount = owners_.signCount;
		ba.total += value;

		emit Transfer(address(0), to, address(token), id, 0, toBalances);
	}

	function onERC1155Received(
			address operator,
			address from,
			uint256 id, uint256 value, bytes calldata data
	) external override returns(bytes4) {
		address[] memory to;
		uint256 signCount;
		(to,signCount) = abi.decode(data, (address[], uint256));

		_onERC1155Received(_isERC1155(msg.sender), from, to, id, value, signCount);

		return _ERC1155_RECEIVED;
	}

	function onERC1155BatchReceived(
			address operator,
			address from,
			uint256[] calldata ids, uint256[] calldata values, bytes calldata data
	) external override returns(bytes4) {
		address[] memory to;
		uint256 signCount;
		(to,signCount) = abi.decode(data, (address[],uint256));

		IERC1155 token = _isERC1155(msg.sender);

		for (uint i = 0; i < ids.length; i++) {
			_onERC1155Received(token, from, to, ids[i], values[i], signCount);
		}

		return _ERC1155_BATCH_RECEIVED;
	}

	function _withdraw(
		address from, address to, address token, uint256 tokenId, uint256 amount, bytes memory _data
	) internal override {
		Balances storage ba = _assets[token][tokenId];
		Owners storage owners = ba.values[from];

		require(amount <= owners.balances, "#ERC1155Proxy#_withdraw: INSUFFICIENT_BALANCES");
		require(amount > 0, "#ERC1155Proxy#_withdraw: INVALID_AMOUNT");

		uint256 formBalances = owners.balances - amount;

		owners.balances = formBalances;
		ba.total -= amount;

		IERC1155(token).safeTransferFrom(address(this), to, tokenId, amount, _data);

		if (formBalances == 0) {
			delete ba.values[from];
		}
		if (ba.total == 0) {
			delete _assets[token][tokenId];
		}

		emit Transfer(from, address(0), token, tokenId, formBalances, 0);
	}

	function _transfer(address from, Owners memory toOwners, address token, uint256 tokenId, uint256 amount) internal override {
		Balances storage ba = _assets[token][tokenId];

		require(amount <= ba.values[from].balances, "#ERC1155Proxy#_transfer: INSUFFICIENT_BALANCES");
		require(amount > 0, "#ERC1155Proxy#_transfer: INVALID_AMOUNT");

		address to = toOwners.owners[0];
		uint256 formBalances = ba.values[from].balances - amount;
		uint256 toBalances = ba.values[to].balances + amount;

		ba.values[from].balances = formBalances;
		ba.values[to] = toOwners;
		ba.values[to].balances = toBalances;

		if (formBalances == 0) {
			delete ba.values[from];
		}

		emit Transfer(from, to, token, tokenId, formBalances, toBalances);
	}

	function balanceOf(address token, uint256 tokenId, address owner) public view override returns(uint256) {
		return _assets[token][tokenId].values[owner].balances;
	}

	function ownersOf(address token, uint256 tokenId, address owner) public view override returns(Owners memory) {
		return _assets[token][tokenId].values[owner];
	}
}