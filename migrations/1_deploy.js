
var ERC721Proxy = artifacts.require("ERC721Proxy.sol");
var ERC721 = artifacts.require("ERC721.sol");

const { deployProxy, upgradeProxy, prepareUpgrade } = require('@openzeppelin/truffle-upgrades');

const fs = require('fs');
const deploy_path = `${__dirname}/../out/deploy.json`;
const pub_path = `${__dirname}/../out/deploy_pub.json`;

async function upgradeDeploy(name, Contract, args, opts) {
	var deploy = {}, pub_json = {};
	var deployer = opts.deployer;

	if (fs.existsSync(deploy_path)) {
		try {
			deploy = JSON.parse(fs.readFileSync(deploy_path, 'utf-8'));
		} catch(err) {}
	}

	var pub, cache = deploy[name];

	if (cache && cache.address) {
		pub = new Contract(cache.address);
		pub.cached = true;

		if (cache.impl == await prepareUpgrade(pub.address, Contract, {deployer})) // 获取实现 impl
			return pub;
	}

	if (!pub)
		// 部署外部上下文,这个协约由`truffle-upgrades`自动自成
		// 调用此协约方法时会间接调用实现`impl`的方法，并且使用当前协约上下文
		pub = await deployProxy(Contract, args, opts);

	await upgradeProxy(pub.address, Contract, {deployer}); // 部署实现 impl

	deploy[name] = {
		address: pub.address, impl: await prepareUpgrade(pub.address, Contract, {deployer}),
	};
	fs.writeFileSync(deploy_path, JSON.stringify(deploy, null, 2));

	var pub_json = {};
	for (var [k,v] of Object.entries(deploy)) {
		pub_json[k] = v.address;
	}
	fs.writeFileSync(pub_path, JSON.stringify(pub_json, null, 2));

	return pub;
}

async function deploy(deployer, name, Contract, args, opts) {
	if (process.env.UPGRADE == 'true') { // 使用升级方式部署协约
		return upgradeDeploy(name, Contract, args, opts);
	} else { // 使用普通方式部署协约每次部署协约地址都会发生改变
		await deployer.deploy(Contract, args, opts);
		return Contract;
	}
}

module.exports = async function(deployer, networks, accounts) {
	// var team = accounts[0];

	// https://docs.openzeppelin.com/upgrades-plugins/1.x/faq#why-cant-i-use-custom-types
	opts = { deployer, initializer: 'initialize', unsafeAllowCustomTypes: true };
	// TODO: check storage layout
	var erc721_proxy = await deploy(deployer, 'ERC721Proxy', ERC721Proxy, [], opts);
	var erc721 = await deploy(deployer, 'ERC721', ERC721, [], opts);

	console.log("ERC721Proxy:", erc721_proxy.address);
	console.log("ERC721      :", erc721.address);
};