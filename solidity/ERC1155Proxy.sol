
pragma solidity ^0.6.12;
pragma experimental ABIEncoderV2;

import './Base.sol';
import './NFTProxy.sol';

contract ERC1155Proxy is IERC1155Receiver, NFTProxy {
	using Address for address;

	struct Balances {
		uint256 total;
		mapping (address => uint256) values; // map( owner => balances )
	}
	// token => map( tokenId => Balances )
	mapping (address => mapping(uint256 => Balances)) internal _balances;

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
		IERC1155 token, address from, address to, uint256 id, uint256 value
	) private {
		if (to == address(0)) {
			to = from;
		}
		require(to != address(0), "#ERC1155Proxy#_onERC1155Received: TO_IS_EMPTY");

		Balances storage ba = _balances[address(token)][id];
		require(
			token.balanceOf(address(this), id) >= ba.total + value,
			"#ERC1155Proxy#_onERC1155Received: INVALID_AMOUNT"
		);

		uint256 toBalances = ba.values[to] + value;
		ba.values[to] = toBalances;
		ba.total += value;

		emit Transfer(address(0), to, address(token), id, 0, toBalances);
	}

	function onERC1155Received(
			address operator,
			address from,
			uint256 id, uint256 value, bytes calldata data
	) external override returns(bytes4) {
		address to;
		(to) = abi.decode(data, (address));

		_onERC1155Received(_isERC1155(msg.sender), from, to, id, value);

		return _ERC1155_RECEIVED;
	}

	function onERC1155BatchReceived(
			address operator,
			address from,
			uint256[] calldata ids, uint256[] calldata values, bytes calldata data
	) external override returns(bytes4) {
		address to;
		(to) = abi.decode(data, (address));

		IERC1155 token = _isERC1155(msg.sender);

		for (uint i = 0; i < ids.length; i++) {
			_onERC1155Received(token, from, to, ids[i], values[i]);
		}

		return _ERC1155_BATCH_RECEIVED;
	}

	function _withdraw(
		address from, address to, address token, uint256 tokenId, uint256 amount, bytes memory _data
	) internal override {
		Balances storage ba = _balances[token][tokenId];

		require(amount <= ba.values[from], "#ERC1155Proxy#_withdraw: INSUFFICIENT_BALANCES");
		require(amount > 0, "#ERC1155Proxy#_withdraw: INVALID_AMOUNT");

		uint256 formBalances = ba.values[from] - amount;

		ba.values[from] = formBalances;
		ba.total -= amount;

		IERC1155(token).safeTransferFrom(address(this), to, tokenId, amount, _data);

		emit Transfer(from, address(0), token, tokenId, formBalances, 0);
	}

	function _transfer(address from, address to, address token, uint256 tokenId, uint256 amount) internal override {
		Balances storage ba = _balances[token][tokenId];

		require(amount <= ba.values[from], "#ERC1155Proxy#_transfer: INSUFFICIENT_BALANCES");
		require(amount > 0, "#ERC1155Proxy#_transfer: INVALID_AMOUNT");

		uint256 formBalances = ba.values[from] - amount;
		uint256 toBalances = ba.values[to] + amount;

		ba.values[from] = formBalances;
		ba.values[to] = toBalances;

		emit Transfer(from, to, token, tokenId, formBalances, toBalances);
	}

	function balanceOf(address token, uint256 tokenId, address owner) public view override returns(uint256) {
		return _balances[token][tokenId].values[owner];
	}
}