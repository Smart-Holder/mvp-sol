
// pragma solidity ^0.7.5;
pragma solidity ^0.6.12;
pragma experimental ABIEncoderV2;

import './base.sol';

abstract contract NFTProxy is MvpBase {

	uint256 private constant _TRANSFER_EXPIRY = 60; // 60 second

	struct Owners {
		uint256 balances; // token 数量
		uint256 signCount; // 签名数量限制,转移资产时最小签名数量
		address[] owners; // owners 第一个索引为主要owner后面的为从owner对外这个资产属于主owner
	}

	struct Signature {
		bytes32 r; bytes32 s; uint8 v;
	}

	struct TransferTx {
		address token;
		uint256 tokenId;
		address from;
		address[] to;
		uint256 amount;
		bytes   data;
		uint256 expiry; // second
		uint256 signCount;
		address[] signer;
		Signature[] rsv;
	}

	event Transfer(
		address indexed from,
		address indexed to,
		address token, uint256 indexed tokenId, uint256 fromBalance, uint256 toBalance
	);

	function _withdraw(address from, address to, address token, uint256 tokenId, uint256 amount, bytes memory _data) virtual internal;
	function _transfer(address from, Owners memory toOwners, address token, uint256 tokenId, uint256 amount) virtual internal;
	function balanceOf(address token, uint256 tokenId, address owner) virtual public view returns(uint256);
	function ownersOf (address token, uint256 tokenId, address owner) virtual public view returns(Owners memory);

	function withdraw(address to, address token, uint256 tokenId, uint256 amount, bytes memory _data) public {
		Owners memory owners = ownersOf(token, tokenId, _msgSender());
		require(owners.signCount == 1, "#NFTProxy#transfer: NO_TRANSFER_SIGN_ERR"); // 如果signCount==1可以转移
		_withdraw(_msgSender(), to, token, tokenId, amount, _data);
	}

	function transfer(address[] memory to, address token, uint256 tokenId, uint256 amount, uint256 signCount) public {
		Owners memory owners = ownersOf(token, tokenId, _msgSender());
		require(owners.signCount == 1, "#NFTProxy#transfer: NO_TRANSFER_SIGN_ERR"); // 如果signCount==1可以转移
		Owners memory toOwners = checkOwners(token, tokenId, to, signCount);
		_transfer(_msgSender(), toOwners, token, tokenId, amount);
	}

	function checkEmptyAddress(address[] memory addrs) internal pure returns(address) {
		require(addrs.length != 0, "#NFTProxy#checkAddressEmpty: ADDRESS_LIST_LENGTH_ZERO");
		return addrs[0];
	}

	function checkOwners(address token, uint256 tokenId, address[] memory owners, uint256 signCount) view internal returns (Owners memory) {
		address owner = checkEmptyAddress(owners);
		Owners memory owners_ = ownersOf(token, tokenId, owner);
		if (owners_.owners.length == 0) {
			require(signCount <= owners.length, "#NFTProxy#checkOwners: BAD_SIGN_COUNT");
			owners_.balances = 1;
			owners_.owners = owners;
			owners_.signCount = signCount;
		}
		return owners_;
	}

	function indexOf(address[] memory addrs, address addr) internal pure returns(int256) {
		for (uint256 i = 0; i < addrs.length; i++) {
			if (addrs[i] == addr) {
				return int256(i);
			}
		}
		return -1;
	}

	function encodePacked(TransferTx memory tx) public pure returns(bytes memory) {
		bytes memory byte_ = abi.encode(
			tx.token, tx.tokenId, tx.from, tx.to, tx.amount, tx.data, tx.expiry, tx.signCount);
		return byte_;
	}

	function verify(TransferTx memory tx) view public {
		require(tx.expiry > block.timestamp, "#NFTProxy#verify: TRANSFER_EXPIRY");

		address token = tx.token;
		uint256 tokenId = tx.tokenId;
		address from = tx.from;
		address[] memory signer = tx.signer;
		Signature[] memory rsv_ = tx.rsv;

		bytes memory buf = encodePacked(tx);
		//bytes memory head = bytes("\x19Ethereum Signed Message:\n");
		bytes32 hash = keccak256(buf);

		Owners memory owners = ownersOf(token, tokenId, from);
		// Owners memory owners;
		// owners.balances = 1;
		// owners.owners = new address[](1);
		// owners.owners[0] = 0xc2C09aABe77B718DA3f3050D0FDfe80D308Ea391;
		// owners.signCount = 1;

		require(from != address(0), "#NFTProxy#verify: ADDRESS_ZERO");
		require(from == owners.owners[0], "#NFTProxy#verify: OWNER_NO_MATCH");
		require(signer.length >= owners.signCount, "#NFTProxy#verify: SIGN_COUNT_TOO_LITTLE");
		require(signer.length == rsv_.length, "#NFTProxy#verify: BAD_RSV_LIST_LENGTH");

		address[] memory addrs = new address[](owners.signCount);
		uint256 signCount = 0;

		for (uint256 i = 0; i < signer.length; i++) {
			address addr = signer[i];
			if (indexOf(addrs, addr) == -1 && indexOf(owners.owners, addr) != -1) { // Exclude duplicates
				Signature memory rsv = rsv_[i];
				address rec = ecrecover(hash, rsv.v, rsv.r, rsv.s);
				// require(rec == addr, "#NFTProxy#verification: ERR_ecrecover");
				if (rec == addr) {
					addrs[signCount] = addr;
					signCount++;
					if (signCount == owners.signCount)
						return;
				}
			}
		}

		require(signCount == owners.signCount, "#NFTProxy#verification: BAD_SIGNATURE");
	}

	function withdrawFrom(TransferTx memory tx) public {
		verify(tx);
		_withdraw(tx.from, tx.to[0], tx.token, tx.tokenId, tx.amount, tx.data);
	}

	function transferFrom(TransferTx memory tx) public {
		verify(tx);
		Owners memory owners = checkOwners(tx.token, tx.tokenId, tx.to, tx.signCount);
		_transfer(tx.from, owners, tx.token, tx.tokenId, tx.amount);
	}

}