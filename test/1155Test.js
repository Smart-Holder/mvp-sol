
var { assert } = require("chai");
var rng = require('somes/rng');
var utils = require('./utils');

contract('1155', (accounts) => {
	var [from,to] = accounts;
	var {ERC1155, ERC1155Proxy} = utils.create(from);

	before(async () => {
	});

	context('ERC1155 and ERC1155Proxy', () =>{
		var ids = [];

		before(async () => {
			for (var i = 0; i < 4; i++) {
				ids.push('0x' + rng.rng(32).toString('hex'));
			}
		});

		it('mint erc1155 tokenId', async () => {
			await ERC1155.mint(from, ids[0], 10, '0x');
			assert((await ERC1155.balanceOf(from, ids[0])).toNumber() == 10);
		});

		it('mintBatch erc1155 tokenId', async () => {
			await ERC1155.mintBatch(from, [ids[1]], [7], '0x');
			assert((await ERC1155.balanceOf(from, ids[1])).toNumber() == 7);
		});

		it('mint erc1155 tokenId to erc1155proxy', async () => {
			await ERC1155.mint(ERC1155Proxy.address, ids[2], 10, web3.eth.abi.encodeParameters(['address'], [from]));
			var balanceOf = (await ERC1155Proxy.balanceOf(ERC1155.address, ids[2], from)).toNumber();
			assert(balanceOf == 10);
		});

		it('mintBatch erc1155 tokenId to erc1155proxy', async () => {
			await ERC1155.mintBatch(ERC1155Proxy.address, [ids[3]], [10], web3.eth.abi.encodeParameters(['address'], [from]));
			assert((await ERC1155Proxy.balanceOf(ERC1155.address, ids[3], from)).toNumber() == 10);
		});

		it('call erc1155 safeTransferFrom', async () => {
			await ERC1155.safeTransferFrom(from, to, ids[1], 2, '0x');
			assert((await ERC1155.balanceOf(to, ids[1])).toNumber() == 2);
		});

		it('call erc1155 safeTransferFrom to ERC1155Proxy', async () => {
			var id = ids[0]
			var balance = (await ERC1155.balanceOf(from, id)).toNumber();
			await ERC1155.safeTransferFrom(
				from, ERC1155Proxy.address, id, balance, web3.eth.abi.encodeParameters(['address'], [to]));
			assert((await ERC1155Proxy.balanceOf(ERC1155.address, id, to)).toNumber() == balance);
		});

		it('call erc1155 safeBatchTransferFrom to ERC1155Proxy', async () => {
			var _ids = ids.slice(1);
			var amounts = [];
			for (var id of _ids) {
				amounts.push((await ERC1155.balanceOf(from, id)).toNumber());
			}
			await ERC1155.safeBatchTransferFrom(
				from, ERC1155Proxy.address, _ids, amounts, web3.eth.abi.encodeParameters(['address'], [to]));
			for (var id of _ids) {
				assert((await ERC1155Proxy.balanceOf(ERC1155.address, id, to)).toNumber() == amounts.shift());
			}
		});

		it('call erc1155proxy transfer', async () => {
			var id = ids[0];
			var balance = (await ERC1155Proxy.balanceOf(ERC1155.address, id, to)).toNumber();
			await ERC1155Proxy.transfer(from, ERC1155.address, id, balance, { from: to });
			assert((await ERC1155Proxy.balanceOf(ERC1155.address, id, to)).toNumber() == 0);
			assert((await ERC1155Proxy.balanceOf(ERC1155.address, id, from)).toNumber() == balance);
		});

		it('call erc1155proxy withdraw', async () => {
			var id = ids[0];
			var balance = (await ERC1155Proxy.balanceOf(ERC1155.address, id, from)).toNumber();
			await ERC1155Proxy.withdraw(from, ERC1155.address, id, balance, '0x', { from });
			assert((await ERC1155Proxy.balanceOf(ERC1155.address, id, from)).toNumber() == 0);
			assert((await ERC1155.balanceOf(from, id)).toNumber() == balance);
		});

	});

});
