
var { assert } = require("chai");
var rng = require('somes/rng');
var utils = require('./utils');

contract('721', (accounts) => {
	var [from,to] = accounts;
	var ERC721, ERC721Proxy;

	before(async () => {
		var app = utils.create(from);
		ERC721 = app.ERC721;
		ERC721Proxy = app.ERC721Proxy;
	})

	context('ERC721 and ERC721Proxy', () =>{

		var ids = [];

		before(async () => {
			for (var i = 0; i < 2; i++) {
				ids.push('0x' + rng.rng(32).toString('hex'));
			}
		});

		it('mint erc721 tokenId', async () => {
			for (var id of ids) {
				await ERC721.mint(id);
				assert(await ERC721.ownerOf(id) == from);
			}
		});

		it('call erc721 safeTransferFrom', async () => {
			await ERC721.safeTransferFrom(from, to, ids[1]);
			assert(await ERC721.ownerOf(ids[1]) == to);
		});

		it('call erc721 safeTransferFrom to ERC721Proxy', async () => {
			for (var id of ids) {
				var from = await ERC721.ownerOf(id);
				await ERC721.methods['safeTransferFrom(address,address,uint256,bytes)'](
					from, ERC721Proxy.address, id, web3.eth.abi.encodeParameters(['address'], [to]), { from });
				assert((await ERC721Proxy.balanceOf(ERC721.address, id, to)).toNumber());
			}
		});

		it('call erc721proxy transfer', async () => {
			await ERC721Proxy.transfer(from, ERC721.address, ids[0], 1, { from: to });
			assert((await ERC721Proxy.balanceOf(ERC721.address, ids[0], from)).toNumber());
		});

		it('call erc721proxy withdraw', async () => {
			await ERC721Proxy.withdraw(from, ERC721.address, ids[0], 1, '0x', { from });
			assert(await ERC721.ownerOf(ids[0]) == from);
		});

	});

});
