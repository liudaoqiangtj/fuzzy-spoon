'''
Ctrl + O class定义中重写特殊方法
def valid_proof(last_proof: int, proof: int) -> bool: 声明函数时给参数添加类型名，"参数：类型"，函数返回类型" -> 类型"
比特币脚本没有for循环，不是图灵完备的
以太坊，去中心化的应用平台，区块量2.0，可编程，智能合约，EVM，每15秒出块，挖矿奖励3ETH，叔块奖励，无总量限制
提供了以太坊虚拟机，沙盒对外隔离(安全），支持高级语言的编程。
以太坊解决了比特币什么问题？比特币脚本限制，比特币脚本语言复杂，开发门槛较高。
智能合约
以太坊上的程序，是代码和数据（状态）的集合，准图灵完备，典型应用：代币,EOS,游戏，合同（去中心化）
Solidity 类JavaScript语言 .sol后缀
contract HelloWorld{
	function hello() public returns(string){
		return "Hello World"
	}
}

Remix , Solidity IDE
运行环境 EVM 以太坊虚拟机 ，Solidity->EVM, Java->JVM

以太坊核心概念-账户
地址（Address）:20字节，状态（State）
EOA外部账户，私钥控制；合约账户（token）
钱包 Geth,Mist,MetaMask 开发者工具

Gas 交易手续费 Gas Limit
最小单位1Wei,10^9Wei = 1GWei,10^12Wei = 1szabo(萨博)，10^15Wei = 1 finey(芬妮)，10^18Wei = 1Ether

公有链：
联盟链： IBM 超级账本，EOS 超级节点
私有链：

去中心化Dapp: 应用层  前端  -APP
					      H5/CSS
					后端  节点
						  存储
			 智能合约
Dapp ,Augur应用

Solidity 语言详解
静态类型语言 值类型 引用类型 ，必须在编译时指定变量类型，例如C++,Java是静态语言，JavaScript是动态语言
bool true/false
整形 int/uint   uint8 步进到uint256
运算符： ^ 异或， ~ 位取反，

数组
T[k] 元素类型为T，固定长度为k地数组；T[] ：元素类型为T,长度动态调整；
byte string 是一种特殊的数组，string
成员 属性length ,函数push()

映射 Mapping
mapping(address => uint) public balances;

全局变量和函数

msg.sender(address)
msg.value(uint)
block.coinbase(address)
block.difficulty(uint)
block.number(uint)
block.timestamp(uint)
now(uint)
tx.gasprice(uint)

错误处理，回退状态，类似数据库的事务的调用
assert
require

可见性 public private  external internal
无名函数类似于C++的析构函数
纯函数  只能进行本地的计算
构造函数
回退函数















'''