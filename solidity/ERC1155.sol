
pragma solidity ^0.6.12;

import './erc1155_.sol';

contract ERC1155 is ERC1155_ {

	function initialize() public {
		__ERC1155_init();
	}

	function mint(address account, uint256 id, uint256 amount, bytes memory data) public {
		_mint(account, id, amount, data);
	}

	function mintBatch(address to, uint256[] memory ids, uint256[] memory amounts, bytes memory data) public {
		_mintBatch(to, ids, amounts, data);
	}

	function burn(address account, uint256 id, uint256 amount) public {
		_burn(account, id, amount);
	}

	function burnBatch(address account, uint256[] memory ids, uint256[] memory amounts) public {
		_burnBatch(account, ids, amounts);
	}

}