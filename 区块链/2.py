#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: liudaoqiang
@file: studycase
@time: 2018/6/23 21:58

Truffle是目前最流行的以太坊开发框架，采用JavaScript编写，支持智能合约的编译、部署和测试。
智能合约必须要部署到链上进行测试。可以选择部署到一些公共的测试链比如Rinkeby或者Ropsten上。
部署到私链上，使用Ganache,truffle develop 客户端

智能合约是一组数据和代码的集合，合约部署到链上以后会产生一个地址，外部通过该地址调用合约
代码来改变或者查询合约的数据（状态）。
metacoin合约是用Solidity语言编写的，通过solc编译成字节码，然后在发生外部访问时被以太坊
虚拟机EVM执行。

Ethereum Main Network; Ropsten Test Network; Kovan Test Network; Rinkeby Test Network

'''
