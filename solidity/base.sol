
pragma solidity ^0.6.12;

import "@openzeppelin/contracts-ethereum-package/contracts/utils/Address.sol";
import "@openzeppelin/contracts-ethereum-package/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts-ethereum-package/contracts/introspection/IERC165.sol";

interface IERC1155 is IERC165 {
	event TransferSingle(address indexed operator, address indexed from, address indexed to, uint256 id, uint256 value);
	event TransferBatch(address indexed operator, address indexed from, address indexed to, uint256[] ids, uint256[] values);
	event ApprovalForAll(address indexed account, address indexed operator, bool approved);
	event URI(string value, uint256 indexed id);
	function balanceOf(address account, uint256 id) external view returns (uint256);
	function balanceOfBatch(address[] calldata accounts, uint256[] calldata ids) external view returns (uint256[] memory);
	function setApprovalForAll(address operator, bool approved) external;
	function isApprovedForAll(address account, address operator) external view returns (bool);
	function safeTransferFrom(address from, address to, uint256 id, uint256 amount, bytes calldata data) external;
	function safeBatchTransferFrom(address from, address to, uint256[] calldata ids, uint256[] calldata amounts, bytes calldata data) external;
}

interface IERC1155MetadataURI is IERC1155 {
	function uri(uint256 id) external view returns (string memory);
}

interface IERC1155Receiver is IERC165 {
	function onERC1155Received(
		address operator,
		address from,
		uint256 id, uint256 value, bytes calldata data
	) external returns(bytes4);

	function onERC1155BatchReceived(
		address operator, address from,
		uint256[] calldata ids, uint256[] calldata values, bytes calldata data
	) external returns(bytes4);
}

contract MvpBase is IERC165 {
	
	bytes4 private constant _INTERFACE_ID_ERC165 = 0x01ffc9a7;

	address private _owner;

	/**
		* @dev Mapping of interface ids to whether or not it's supported.
		*/
	mapping(bytes4 => bool) private _supportedInterfaces;

	event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

	constructor() public {  // payable
		_owner = _msgSender();
		_registerInterface(_INTERFACE_ID_ERC165);
	}

	/**
		* @dev See {IERC165-supportsInterface}.
		*
		* Time complexity O(1), guaranteed to always use less than 30 000 gas.
		*/
	function supportsInterface(bytes4 interfaceId) public view override returns (bool) {
			return _supportedInterfaces[interfaceId];
	}

	/**
		* @dev Registers the contract as an implementer of the interface defined by
		* `interfaceId`. Support of the actual ERC165 interface is automatic and
		* registering its interface id is not required.
		*
		* See {IERC165-supportsInterface}.
		*
		* Requirements:
		*
		* - `interfaceId` cannot be the ERC165 invalid interface (`0xffffffff`).
		*/
	function _registerInterface(bytes4 interfaceId) internal virtual {
			require(interfaceId != 0xffffffff, "ERC165: invalid interface id");
			_supportedInterfaces[interfaceId] = true;
	}

	/**
		* @dev Throws if called by any account other than the owner.
		*/
	modifier onlyOwner() {
		require(_owner == _msgSender(), "Ownable: caller is not the owner");
		_;
	}

	/**
		* @dev Returns the address of the current owner.
		*/
	function owner() public view returns (address) {
		return _owner;
	}

	/**
		* @dev Leaves the contract without owner. It will not be possible to call
		* `onlyOwner` functions anymore. Can only be called by the current owner.
		*
		* NOTE: Renouncing ownership will leave the contract without an owner,
		* thereby removing any functionality that is only available to the owner.
		*/
	function renounceOwnership() public virtual onlyOwner {
		emit OwnershipTransferred(_owner, address(0));
		_owner = address(0);
	}

	/**
		* @dev Transfers ownership of the contract to a new account (`newOwner`).
		* Can only be called by the current owner.
		*/
	function transferOwnership(address newOwner) public virtual onlyOwner {
		require(newOwner != address(0), "Ownable: new owner is the zero address");
		emit OwnershipTransferred(_owner, newOwner);
		_owner = newOwner;
	}

	function _msgSender() internal view virtual returns (address payable) {
		return msg.sender;
	}

	function _msgData() internal view virtual returns (bytes memory) {
		this; // silence state mutability warning without generating bytecode - see https://github.com/ethereum/solidity/issues/2691
		return msg.data;
	}
}
