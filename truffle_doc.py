'''
QUICKSTART 快速开始
truffle unbox metacoin
contracts/Migrations.sol 管理和更新智能合约的状态
migrations/1_initial_deployment.js 部署Migrations.sol合约的脚本
migrations/2_deploy_contracts/js 以数字按顺序开头，MetaCoin合约的部署脚本
truffle.js Truffle 的配置文件

Compiling Contracts 编译合约
truffle compile 编译智能合约，生成build，合约文件对应的json文件

MIGRATIONS 部署
4_example_migration.js 合约部署脚本以数字开头
var MyContract = artifacts.require("MyContract");
module.exports = function(deployer) {
  // deployment steps
  deployer.deploy(MyContract);
};
artifacts.require(合约名)
module.exports
contracts/Migrations.sol作为初始合约，不会更新

DEPLOYER 部署函数
	例子
deployer.deploy(A).them(function)(){
	return deployer.deploy(B,A.address)
}

NETWORKS CONSIDERATIONS 网络条件
可以根据网络的情况有条件的部署
module.exports = function(deployer, network) {
	if (network == "live"){
		// Do something specific to the network named "live"
	}else{
		//Perform a different step otherwise
	}
}

AVAILABLE ACCOUNTS 可用账户
module.experts还可以向部署函数传递以太坊客户端和web服务器提供的账户，可以在部署期间使用。
module.experts = function(deployer, network, accounts){
	//use the accounts within your migrations
}

DEPLOYER API 部署函数API
deployer.deploy();
deployer.deploy(A) 不带构造函数变量
deployer.deploy(A,arg1,arg2,...) 带有构造函数变量
deployer.deploy(A,{overwrite: false}) 如果合约已经部署就不再部署
deployer.deploy(A, {gas:4612388,from :"0x....."}) 设置gas的最大值，和from地址
deployer.link(LibA,[B,C,D]) 把已经部署的合约链接到,B,C,D三个合约


'''