pragma solidity ^0.4.24;

contract Context {
	address __impl;
	uint256[50] __gap;
	
	// function delegateCall(bytes data) public {
	//     this.call.value(msg.value)(data);
	// }

	// function getPositionAt(uint n) public view returns (address) {
	//     assembly {
	//         let d := sload(n)
	//         mstore(0x80, d)
	//         return(0x80,32)
	//   }
	// }

	constructor(address impl) {
		require(impl != address(0));
		__impl = impl;
	}

	function() payable public {
		address _impl = __impl;
		require(_impl != address(0));

		assembly {
			let ptr := mload(0x40) 
			calldatacopy(ptr, 0, calldatasize) 
			let result := delegatecall(gas, _impl, ptr, calldatasize, 0, 0)
			let size := returndatasize 
			returndatacopy(ptr, 0, size) 

			switch result
			case 0 { revert(ptr, size) }
			default { return(ptr, size) }
		}
	}

}

contract Logic {
	address public impl;
	uint256 public a;
	uint256 public b;
	uint256 public c;

	function upgrade(address _impl) public {
		impl = _impl;
	}

	function A(uint256 v) public {
		a = v;
	}

	function B(uint256 v) public {
		b = v;
	}

	function C(uint256 v) public {
		c = v;
	}
}