
var fs = require('fs');
var somes = require('somes').default;
var crypto_tx = require('somes').default;

var ERC721 = artifacts.require("ERC721.sol");
var ERC1155 = artifacts.require("ERC1155.sol");
var ERC721Proxy = artifacts.require("ERC721Proxy.sol");
var ERC1155Proxy = artifacts.require("ERC1155Proxy.sol");

function create(from) {
	var addr = JSON.parse(fs.readFileSync(`${__dirname}/../out/deploy_pub.json`, 'utf-8'));
	return {
		ERC721: new ERC721(addr.ERC721, {from}),
		ERC1155: new ERC1155(addr.ERC1155, {from}),
		ERC721Proxy: new ERC721Proxy(addr.ERC721Proxy, {from}),
		ERC1155Proxy: new ERC1155Proxy(addr.ERC1155Proxy, {from}),
	};
}

async function sign(from, to, token, tokenId, amount, data, privKey) {
	var balance = await this.balanceOf(token, tokenId, from);
	somes.assert(balance, '#ApiIMPL#_tx: NOT_OWN_TOKEN');
	var expiry = Math.floor((Date.now() + 6e4) / 1e3);
	var msg = crypto_tx.message(
		[token, tokenId, to, amount, data || '0x', expiry],
		['address', 'uint256', 'address', 'uint256', 'bytes', 'uint256']
	);
	var {signature,recovery} = crypto_tx.sign(msg, privKey);
	var tx = {
		token, tokenId, to, amount, expiry: BigInt(expiry),
		data: data || '0x',
		rsv: {
			r: '0x' + signature.slice(0, 32).toString('hex'),
			s: '0x' + signature.slice(32, 64).toString('hex'),
			v: recovery + 27,
		},
	};
	return tx;
}

module.exports = {
	create, sign
}