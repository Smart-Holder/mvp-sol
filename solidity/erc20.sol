// SPDX-License-Identifier: MIT
// Created by NTFSWAP Team

pragma solidity ^0.6.12;

import './base.sol';
import "@openzeppelin/contracts-ethereum-package/contracts/token/ERC20/ERC20.sol";

contract ERC20 is Proxyable, ERC20UpgradeSafe {

	function initialize() external {
		__Ownable_init();
		__ERC20_init("MVP", "MVP");
	}

	function mint(uint256 amount) public onlyOwner {
		_mint(msg.sender, tokenId);
	}

	function burn(uint256 amount) public onlyOwner {
		_burn(msg.sender, amount);
	}

}
