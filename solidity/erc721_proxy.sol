// SPDX-License-Identifier: MIT
// Created by NTFSWAP Team

// pragma solidity ^0.7.5;
pragma solidity ^0.6.12;
pragma experimental ABIEncoderV2;

import "./nft_proxy.sol";
import "@openzeppelin/contracts-ethereum-package/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts-ethereum-package/contracts/token/ERC721/IERC721.sol";

contract ERC721Proxy is IERC721Receiver, NFTProxy {
	using Address for address;

	// token => map( tokenID => Owners )
	mapping(address => mapping(uint256 => Owners)) internal _assets;

	bytes4 private constant _ERC721_RECEIVED = 0x150b7a02;
	bytes4 private constant _INTERFACE_ID_ERC721 = 0x80ac58cd;

	function initialize() public {
		__NFTProxy_init();
	}

	// @dev convert addr to standard ERC721 NFT,will be revered if add is invalid.
	function _isERC721(address addr) internal view returns (IERC721) {
		require(
			addr.isContract(),
			"#ERC721Proxy#_isERC721: INVLIAD_CONTRACT_ADDRESS"
		);
		require(
			IERC721(addr).supportsInterface(_INTERFACE_ID_ERC721),
			"The NFT contract has an invalid ERC721 implementation"
		);
		return IERC721(addr);
	}

	function onERC721Received(
			address operator, address from, uint256 tokenId, bytes memory data
	) external override returns (bytes4) {
		IERC721 token = _isERC721(msg.sender);
		require(token.ownerOf(tokenId) == address(this), "#ERC721Proxy#onERC721Received: NOT_OWN_TOKEN");

		address[] memory to;
		uint256 signCount;
		(to,signCount) = abi.decode(data, (address[], uint256));

		checkEmptyAddress(to);

		require(signCount != 0 && signCount <= to.length, "#ERC721Proxy#onERC721Received: BAD_MIN_SIGN_ZERO");

		Owners storage owners = _assets[address(token)][tokenId];
		owners.owners = to; // assign
		owners.signCount = signCount;
		owners.balances = 1;

		emit Transfer(address(0), to[0], address(token), tokenId, 0, 1);

		return _ERC721_RECEIVED;
	}

	function _withdraw(
		address from, address to, address token, uint256 tokenId, uint256 amount, bytes memory _data
	) internal override {
		require(amount == 1, "#ERC721Proxy#_withdraw: AMOUNT_ONLY_BE_1");

		delete _assets[token][tokenId];

		IERC721(token).safeTransferFrom(address(this), to, tokenId, _data);

		emit Transfer(from, address(0), token, tokenId, 0, 1);
	}

	function _transfer(address from, Owners memory toOwners, address token, uint256 tokenId, uint256 amount) internal override {
		require(amount == 1, "#ERC721Proxy#_transfer: AMOUNT_ONLY_BE_1");

		_assets[token][tokenId] = toOwners;

		emit Transfer(from, toOwners.owners[0], token, tokenId, 0, 1);
	}

	function balanceOf(address token, uint256 tokenId, address owner) public view override returns(uint256) {
		address[] storage owners = _assets[token][tokenId].owners;
		return owners.length != 0 && owners[0] == owner ? 1: 0;
	}

	function ownersOf(address token, uint256 tokenId, address owner) public view override returns(Owners memory) {
		return _assets[token][tokenId];
	}

}