#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: liudaoqiang
@file: studycase
@time: 2018/6/23 10:04


EIPS Ethereum Improvement Proposals reposity
ERC-20 合约的标准接口，客户端API，核心协议说明
Abstract 摘要 以下标准允许在智能合约中使用代币的标准API。该标准提供了代币转账的基本api，并且为代币提供证明，以便链上的其他第三方可以使用代币。
Motivation 目的 标准接口目的在于允许以太坊上的任何代币可以被其他应用重复使用，包括钱包到去中心化交易应用。
Specification 说明
Token 代币
Methods 方法
NOTE：ERC-20标准接口使用者必须处理函数返回false导致交易失败的情况，不能认为函数不会返回false.
name
返回代币的名字，例如“MyToken”
OPTIONAL - 可选参数可以提高接口稳定性，但是不是ERC-20标准接口所必须的
	function name() view returns (string name)

symbol
返回代币的标志，例如“HIX”
OPTIONAL - 可选参数可以提高接口稳定性，但是不是ERC-20标准接口所必须的
	function symbol() view returns (string symbol)

decimals
返回代币的小数位数
OPTIONAL - 可选参数可以提高接口稳定性，但是不是ERC-20标准接口所必须的
	function decimals() view returns (uint8 decimals)

totalSupply
返回代币的总量
	function totalSupply() view returns (uint256 totalSupply)

balanceOf
返回地址上的代币余额
	function balanceOf(address _owner) view returns (uint256 balance)

transfer
转账_value数目的代码到地址 _to，并且必须触发 Transfer 事件,该函数应该被 throw 如果账户余额不足以转账；
注意：转账 0 个代币必须被视为是正常转账，并且要触发transfer事件
	function transfer(address _to, uint256 _value) returns (bool success)

transferFrom
从 _from 地址转账 _value 数目的代币到 _to 地址，并且必须触发Transfer事件
transferFrom 方法用于撤销工作流，允许合约代表你转账代币。例如，这允许合约代表你转账代币或者以子币收取费用，这个函数应该 throw
如果触发 _from 账户通过某种机制故意授权消息发送者
注意：转账 0 个代币必须被视为是正常转账，并且要触发Transfer事件
	function transfer(address _from, address _to, uint256 _value) returns (bool success)

approve
允许 _spender账户多次从账户中提取，直到_value余额，如果再次调用该函数 _value 应该覆盖当前的配额
注意：为了防止被攻击，客户端应该确保以这样的方式创建界面，即对同一 _spender 而言，_value 在被设置为其他值之前应该被初始化为0，
尽管合约本身不执行这个操作，后向兼容以前部署的合约。
	function approve(address _spender, uint256 _value) returns (bool success)

allowance
返回 _spender 可以从 _owner 提取的代币数目
	function allowance(address _owner, address _spender) view returns (uint256 remaining)

Events

Transfer
合约必须触发Transfer事件，包括0代币转账
新发行的代币合约应该触发一个Transfer事件，将 _from 地址设置为 0x0
	event Transfer(address indexed _from, address indexed _to, uint256 _value)

Approval
任何成功调用approve()方法都会触发Approval方法
	event Approval(address indexed _owner, address indexed _spender, uint256 _value)

Implementation
在以太坊平台上已经部署了ERC-20兼容的大量合约，不同的实施由不同的团队编写，这些团队有不同的权衡：从节省gas到提高安全性。




'''