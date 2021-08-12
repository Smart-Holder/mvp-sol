
pragma solidity ^0.6.12;

import './ERC1155_0.sol';

contract ERC1155 is ERC1155_0 {

	function initialize() public {
		__ERC1155_0_init();
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