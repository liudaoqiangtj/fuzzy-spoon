/*
 * NB: since truffle-hdwallet-provider 0.0.5 you must wrap HDWallet providers in a 
 * function when declaring them. Failure to do so will cause commands to hang. ex:
 * ```
 * mainnet: {
 *     provider: function() { 
 *       return new HDWalletProvider(mnemonic, 'https://mainnet.infura.io/<infura-key>') 
 *     },
 *     network_id: '1',
 *     gas: 4500000,
 *     gasPrice: 10000000000,
 *   },
 */
var mnemonic = "distance nice vehicle exact elegant range nurse staff attract crouch toast struggle";
var HDWalletProvider = require("truffle-hdwallet-provider");
infura_apikey = 'e1e7410b846f4d2aa22d5b4351613153';
module.exports = { 
  networks: { 
    ropsten: { 
      provider: new HDWalletProvider(mnemonic, 'https://mainnet.infura.io/<infura-key>'),
      network_id: 3 ,
      gas:2022333,
      gasPrice:30000000000
    },
    development:{
      host:"127.0.0.1",
      port:7545,
      network_id:"*"
    },
    private:{
      host:"127.0.0.1",
      port:8545,
      network_id:"*"
    }
  } 
};
