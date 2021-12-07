
// pragma solidity ^0.7.5;
pragma solidity ^0.6.12;
pragma experimental ABIEncoderV2;

import './Base.sol';

abstract contract NFTProxy is Proxyable {

	uint256 private constant _TRANSFER_EXPIRY = 60; // 60 second

	struct Signature {
		bytes32 r; bytes32 s; uint8 v;
	}

	struct TransferTx {
		address token;
		uint256 tokenId;
		address[] to;
		uint256 amount;
		bytes   data;
		uint256 expiry; // second
		address[] from;
		Signature[] rsv;
	}

	event Transfer(
		address indexed from,
		address indexed to,
		address token, uint256 indexed tokenId, uint256 fromBalance, uint256 toBalance
	);

	function __NFTProxy_init() internal {
		__Proxyable_init();
	}

	function deposit(address to, address token, uint256 tokenId, uint256 amount) virtual public {}
	function _withdraw(address from, address to, address token, uint256 tokenId, uint256 amount, bytes memory _data) virtual internal;
	function _transfer(address from, address[] memory to, address token, uint256 tokenId, uint256 amount) virtual internal;
	function balanceOf(address token, uint256 tokenId, address owner) virtual public view returns(uint256);

	function withdraw(address to, address token, uint256 tokenId, uint256 amount) public {
		_withdraw(msg.sender, to, token, tokenId, amount, "");
	}

	function withdraw(address to, address token, uint256 tokenId, uint256 amount, bytes memory _data) public {
		_withdraw(msg.sender, to, token, tokenId, amount, _data);
	}

	function transfer(address[] memory to, address token, uint256 tokenId, uint256 amount) public {
		_transfer(msg.sender, to, token, tokenId, amount);
	}

	function checkEmptyAddress(address[] memory addrs) internal {
		require(addrs.length != 0, "#NFTProxy#checkAddressEmpty: ADDRESS_IS_LENGTH_ZERO");
		//for (uint256 i = 0; i < addrs.length; i++) {
		//	require(addrs[i] != address(0), "#NFTProxy#checkAddressEmpty: ADDRESS_IS_EMPTY");
		//}
	}

	function verification(bytes32 hash, address[] memory from, Signature[] memory rsv_) internal {
		checkEmptyAddress(from);
		for (uint256 i = 0; i < from.length; i++) {
			Signature memory rsv = rsv_[i];
			address addr = ecrecover(hash, rsv.v, rsv.r, rsv.s);
			require(from[i] == addr, "#NFTProxy#verification: BAD_SIGNATURE");
		}
	}

	function withdrawFrom(TransferTx memory tx) public returns(bytes32, address) {
		require(tx.expiry > block.timestamp, "#NFTProxy#withdrawFrom: TRANSFER_EXPIRY");
		bytes32 hash = keccak256(abi.encodePacked(tx.token, tx.tokenId, tx.to, tx.amount, tx.data, tx.expiry));
		verification(hash, tx.from, tx.rsv);
		_withdraw(tx.from[0], tx.to[0], tx.token, tx.tokenId, tx.amount, tx.data);
		return (hash, tx.from[0]);
	}

	function transferFrom(TransferTx memory tx) public returns(bytes32, address) {
		require(tx.expiry > block.timestamp, "#NFTProxy#transferFrom: TRANSFER_EXPIRY");
		bytes32 hash = keccak256(abi.encodePacked(tx.token, tx.tokenId, tx.to, tx.amount, tx.data, tx.expiry));
		verification(hash, tx.from, tx.rsv);
		checkEmptyAddress(tx.to);
		_transfer(tx.from[0], tx.to, tx.token, tx.tokenId, tx.amount);
		return (hash, tx.from[0]);
	}

}