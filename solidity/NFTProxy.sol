
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
		address to;
		uint256 amount;
		bytes   data;
		uint256 expiry; // second
		Signature rsv;
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
	function _withdraw(
		address from, address to, address token, uint256 tokenId, uint256 amount, bytes memory _data) virtual internal;
	function _transfer(address from, address to, address token, uint256 tokenId, uint256 amount) virtual internal;
	function balanceOf(address token, uint256 tokenId, address owner) virtual public view returns(uint256);

	function withdraw(address to, address token, uint256 tokenId, uint256 amount) public {
		_withdraw(msg.sender, to, token, tokenId, amount, "");
	}

	function withdraw(address to, address token, uint256 tokenId, uint256 amount, bytes memory _data) public {
		_withdraw(msg.sender, to, token, tokenId, amount, _data);
	}

	function transfer(address to, address token, uint256 tokenId, uint256 amount) public {
		_transfer(msg.sender, to, token, tokenId, amount);
	}

	function withdrawFrom(TransferTx memory tx) public returns(bytes32, address) {
		require(tx.expiry > block.timestamp, "#NFTProxy#withdrawFrom: TRANSFER_EXPIRY");
		bytes32 hash = keccak256(abi.encodePacked(tx.token, tx.tokenId, tx.to, tx.amount, tx.data, tx.expiry));
		address from = ecrecover(hash, tx.rsv.v, tx.rsv.r, tx.rsv.s);
		_withdraw(from, tx.to, tx.token, tx.tokenId, tx.amount, tx.data);
		return (hash, from);
	}

	function transferFrom(TransferTx memory tx) public returns(bytes32, address) { // external {
		require(tx.expiry > block.timestamp, "#NFTProxy#transferFrom: TRANSFER_EXPIRY");
		bytes32 hash = keccak256(abi.encodePacked(tx.token, tx.tokenId, tx.to, tx.amount, tx.data, tx.expiry));
		address from = ecrecover(hash, tx.rsv.v, tx.rsv.r, tx.rsv.s);
		_transfer(from, tx.to, tx.token, tx.tokenId, tx.amount);
		return (hash, from);
	}

}