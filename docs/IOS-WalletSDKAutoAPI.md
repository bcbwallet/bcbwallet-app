## API

### sdk_registApp

注册应用

#### 请求格式

参数

| name   | type   | required | description |
| :----- | :----- | :------- | :---------- |
| AppID  | string | yes      | 应用ID      |
| pushID | string | yes      | 推送ID      |

请求示例

```json
{
	"method": "sdk_registApp",
	"params": {
		"AppID": "1",
        "pushID":""
	}
}
```

返回示例

```json
{
    "code":0,
    "msg":"ok",
	"result": {}
}
```

###  sdk_setLanguage

设置返回msg语言类型

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| language | string     | yes        | *cn：中文、en：English* |

请求示例
```json
{
	"method": "sdk_setLanguage",
	"params": {
		"language": "en",
	}
}
```

返回示例
```json
{
    "code":0,
    "msg":"ok",
	"result": {}
}
```

### sdk_setWalletDebug

设置开发环境

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| walletDebug | int  | yes        | 钱包管理链环境（*0：研发链、1：测试链、2：正式链*） |
| otcDebug | int  | yes        | OTC及闪兑模块链环境（*0：研发链、1：测试链、2：正式链*） |

请求示例
```json
{
	"method": "sdk_setWalletDebug",
	"params": {
		"walletDebug": 0,
		"otcDebug": 2
	},
}
```

返回示例
```json
{
    "code":0,
    "msg":"ok",
	"result": {}
}
```

### sdk_loadAllChains

获取主链及所有侧链信息 

#### 请求格式
请求示例
```json
{
	"method": "sdk_loadAllChains",
	"params": {}
}
```

返回示例
```json
{
    "code":0,
	"msg": "ok",
    "result": [
        "bcb",
        "yy",
        "jiujiu"
    ]
}
```

### sdk_setWalletChain
链环境设置

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| chainId | string     | yes        | 链ID，传空字符串则重置为主链节点 |

请求示例
```json
{
	"method": "sdk_setWalletChain",
	"params": {
		"chainId": "devtest"
	}
}
```

返回示例
```json
{
    "code":0,
    "msg":"ok",
	"result": {}
}
```

### sdk_getDomainList
获取域名列表 

#### 请求格式
请求示例
```json
{
	"method": "sdk_getDomainList",
	"params": {}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
    "result": [
        "https://wallet.bcbchain.io",
        "https://wallet2.bcbchain.io",
        "https://api.n8.app"
    ]
}
```

### sdk_setWalletDomain
域名设置

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| domain | string | 是       | 域名地址，不能为空 |

请求示例
```json
{
    "method": "setWalletDomain",
	"params": {
		"domain": "https://wallet2.bcbchain.i7",
	}
}
```

#### 返回格式
```json
{
    "code":0,
    "msg":"操作成功",
	"result": {}
}
```

### sdk_createWallet
创建新钱包

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| name      | string | 是       | 钱包名称         |
| password  | string | 是       | 钱包密码         |
| recommend | string | 否       | 推荐人的钱包地址 |

请求示例
```json
{
	"method": "sdk_createWallet",
	"params": {
		"name": "myWallet",
		"password": "qwer1234",
		"recommend": ""
	}
}
```

#### 返回格式
返回示例
```json
{
  "msg" : "Create wallet successful",
  "result" : {
    "name" : "myWalle1t",
    "mnemonicWords" : "0xDE916F4E9D4A7A2CEB99CC6550B1FCCF85C83E30F167E5EACE508431288464CD2194DE32AF410CEC2FB36C0E712A891B0C141BA8CAF6B7A413D199E7B607DF334085E482398F129BEC84095E82D512F0",
    "walletAddr" : "devtestKxUqYy5yupFYRaex8vqW7ET3Rpa1R6Fyq"
  },
  "code" : 0
}
```


### sdk_importPrivateKey
导入私钥生成钱包

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| name      | string | 是       | 钱包名称         |
| key       | string | 是       | 私钥             |
| password  | string | 是       | 钱包密码         |
| recommend | string | 否       | 推荐人的钱包地址 |

请求示例
```json
{
	"method": "sdk_importPrivateKey",
	"params": {
		"name": "myWallet",
		"key": "0xFD774E4D…21087855"，
		"password": "qwer1234",
		"recommend": ""
	}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result": 
	{	
		"name":"myWallet",
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
	}
}
```

### sdk_importKeystore
导入Keystore生成钱包

#### 请求格式
参数
| name      | type   | required | description      |
| :-------- | :----- | :------- | :--------------- |
| name      | string | 是       | 钱包名称         |
| key       | string | 是       | Keystore         |
| password  | string | 是       | 钱包密码         |
| recommend | string | 否       | 推荐人的钱包地址 |

请求示例

```json
{
	"method": "sdk_importKeystore",
	"params": {
		"name": "myWallet",
		"key": ".........."，
		"password": "qwer1234",
		"recommend": ""
	}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result": 
	{	
		"name":"myWallet",
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
	}
}
```

### sdk_importMnemonicWords
导入助记词生成钱包

#### 请求格式
参数

| name      | type   | required | description      |
| :-------- | :----- | :------- | :--------------- |
| name      | string | 是       | 钱包名称         |
| key       | string | 是       | 助记词           |
| password  | string | 是       | 钱包密码         |
| recommend | string | 否       | 推荐人的钱包地址 |

请求示例

```json
{
	"method": "sdk_importMnemonicWords",
	"params": {
		"name": "myWallet",
		"key": ".........."，
		"password": "qwer1234",
		"recommend": ""
	}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result": 
	{	
		"name":"myWallet",
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
	}
}
```

### sdk_getWallets
获取所有钱包信息

#### 请求格式
请求示例
```json
{
	"method": "sdk_getWallets",
	"params": {}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result": 
	[
        {
            "name":"myWallet",
            "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
        },
        {
            "name":"newWallet",
            "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU"
        }
	]
}
```
###  sdk_getMnemonicWords

导出助记词

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| walletAddr | string     | yes        | 钱包地址      |
| password | string | yes | 钱包密码 |

请求示例
```json
{
    "method": "sdk_getMnemonicWords",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "password":"qwer1234"
    }
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
    "msg":"",
	"result": {
        "mnemonicWords":"eyebrow indoor orbit cinnamon hour gain category spawn walk bind spread clinic",		
	}
}
```

### sdk_exportPrivateKey
导出私钥

#### 请求格式
参数
| name       | type   | required | description |
| :--------- | :----- | :------- | :---------- |
| walletAddr | string | yes      | 钱包地址    |
| password   | string | yes      | 钱包密码    |

请求示例

```json
{
    "method": "sdk_exportPrivateKey",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "password":"qwer1234"
    }
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result": 
	{				 "privateKey":"0x98BB2E49822A48728E3CBCFD1A933C1FC500A6204453E7DB85F84EFB90146600"
	}
}
```

### sdk_exportKeystore
导出Keystore

#### 请求格式
参数
| name       | type   | required | description |
| :--------- | :----- | :------- | :---------- |
| walletAddr | string | yes      | 钱包地址    |
| password   | string | yes      | 钱包密码    |

请求示例

```json
{
    "method": "sdk_exportKeystore",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "password":"qwer1234"
    }
}
```

#### 返回格式
返回示例
```json
{
	"code": 0,
	"msg": "ok",
	"result": {
		"keystore": "{\"address\":\"bcbMd6xUDQLoivMT45Qp8o7M8vjN5wRyHAF3\",\"crypto\":{\"cipher\":\"aes-128-ctr\",\"cipherparams\":{\"iv\":\"026fad88d89baadb9110ae533ef8039d\"},\"ciphertext\":\"7c1dafc7e541cc14d0fe11773fc4d2da6933384d5279984df57693f98d3be4a8\",\"kdf\":\"scrypt\",\"kdfparams\":{\"dklen\":32,\"n\":262144,\"p\":1,\"r\":8,\"salt\":\"c1fe07bed958a78763ac5816c7dbad9351accd80c18bbc70aa3279d5fb34638f\"},\"mac\":\"d6042cf16b55c3bac25f392d1d33476e84e5276b672ad8e77ccd1713d586e18d\"},\"id\":\"eabffab4-5c21-46a4-a709-9699a72d1339\",\"version\":3}"
	}
}
```

### sdk_verifyPassword
验证钱包密码

#### 请求格式
参数
| name       | type   | required | description |
| :--------- | :----- | :------- | :---------- |
| walletAddr | string | yes      | 钱包地址    |
| password   | string | yes      | 钱包密码    |

请求示例

```json
{
    "method": "sdk_verifyPassword",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "password":"qwer1234"
    }
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result": {}
}
```

### sdk_changePassword
修改钱包密码

#### 请求格式
参数
| name        | type   | required | description |
| :---------- | :----- | :------- | :---------- |
| walletAddr  | string | yes      | 钱包地址    |
| oldPassword | string | yes      | 原钱包密码  |
| newPassword | string | yes      | 新钱包密码  |

请求示例

```json
{
    "method": "sdk_changePassword",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "oldPassword":"qwer1234",
        "newPassword":"qwer1234"
    }
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result": {}
}
```

### sdk_changeWalletName
修改钱包名称

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| walletAddr | string     | yes        | 钱包地址 |
| newName | string     | yes        | 新钱包地址 |

请求示例
```json
{
    "method": "sdk_changeWalletName",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "newName":"newWallet"
    }
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
    "result": {
        "name":"newWallet",
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5",
    }
}
```

### sdk_deleteWallet
删除钱包

#### 请求格式
参数
| name       | type   | required | description |
| :--------- | :----- | :------- | :---------- |
| walletAddr | string | yes      | 钱包地址    |
| password   | string | yes      | 钱包密码    |

请求示例

```json
{
    "method": "sdk_deleteWallet",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "password":"qwer1234"
    }
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
    "msg":"",
	"result": {}
}
```

### sdk_walletTransation
钱包转账

#### 请求格式
参数
| 字段名     | 类型   | 必须 | 说明                                              |
| ---------- | ------ | ---- | ------------------------------------------------- |
| walletAddr | string | 是   | 钱包地址                                          |
| password   | string | 是   | 钱包密码                                          |
| coinAddr   | string | 是   | 要转账币种的合约地址                              |
| toAddr     | string | 是   | 转账到的目标地址                                  |
| value      | string | 是   | 转账的金额，例如"102.23"                          |
| note       | string | 否   | 转账的备注，对于BCB链，这个字段最终会写入到区块中 |
| byb        | string | 是   | 是否为BYB转账                                     |

#### 请求示例

```json
{
	"method": "sdk_walletTransation",
	"params": {
		"walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "password":"qwer1234",
        "coinAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "toAddr":"bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "value":"0.1",
        "note":"转账",
        "byb":"0"
	}
}
```

#### 返回格式
结果
- txHash：交易hash

返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result": 
	{	
		"txHash":"0x0F8642968E48A16316CD499BF142E15EEFF03BE44816796AF87DDC2F1B72BBA4",
	}
}
```

### sdk_walletCommonPay

#### 请求格式
参数
| 字段名     | 类型   | 必须 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| walletAddr | string | 是   | 钱包地址                                                     |
| version    | Int    | 是   | 1.0的支付传1， 2.0的支付传2                                  |
| password   | string | 是   | 钱包密码                                                     |
| walletCall | string | 是   | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |

**示例：walletCall字符串格式**

```java
"{\"note\":\"ApplyToBanker\",\"gasLimit\":\"3500000\",\"contractCall\":[{\"contractAddr\":\"bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ\",\"methodName\":\"Transfer\",\"methodParams\":[{\"type\":\"types.Address\",\"value\":\"bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH\"},{\"type\":\"bn.Number-decimal\",\"value\":\"0.0001\"}],\"methodRet\":\"\"}]}"
```

请求示例

```json
{
	"method": "sdk_walletCommonPay",
	"params": {
		"walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "version":"2",
        "password":"qwer1234",
        "walletCall":"{\"note\":\"ApplyToBanker\",\"gasLimit\":\"3500000\",\"contractCall\":[{\"contractAddr\":\"bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ\",\"methodName\":\"Transfer\",\"methodParams\":[{\"type\":\"types.Address\",\"value\":\"bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH\"},{\"type\":\"bn.Number-decimal\",\"value\":\"0.0001\"}],\"methodRet\":\"\"}]}"
	}
}
```

#### 返回格式
```json
{
    "code":0,
	"msg": "ok",
	"result": 
	{	
        "txHash":"0x0F8642968E48A16316CD499BF142E15EEFF03BE44816796AF87DDC2F1B72BBA4"
	}
}
```

### sdk_getAddrsBalance

#### 请求格式

参数
| 字段名      | 类型   | 必须 | 说明                                           |
| ----------- | ------ | ---- | ---------------------------------------------- |
| walletAddr  | string | 是   | 钱包地址                                       |
| legalSymbol | string | 是   | 资产的法币计价单位，人民币为：CNY；美元为：USD |

#### 请求示例

```json
{
	"method": "sdk_getAddrsBalance",
	"params": {
		"walletAddr": "bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9",
		"legalSymbol": "CNY"
	}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result":[
        {
            "addr":"bcbtestCTLvcA7pa1RqCncL2fRcALgRrVYudJNeE",
            "coinType":"0x1001",
            "conAddr":"bcbtestAtEJ4dTejwJReKA4dtFjy9cQ3HzR6jbwF",
            "name":"BCBT",
            "symbol":"BCBT",
            "balance":"101",
            "last":"2019-04-01T14:21:00.8342387+08:00",
            "decimals":"9",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/BCBMainNet.png",
            "legalValue":"688.8604",
            "isToken":false,
            "idx":0,
            "feeInfo":null
        },
        {
            "addr":"bcbtestCTLvcA7pa1RqCncL2fRcALgRrVYudJNeE",
            "coinType":"0x1001",
            "conAddr":"bcbtestDhxdEq9JPFhQ8xicUdSAHQHxymP2orXYW",
            "name":"B99",
            "symbol":"B99",
            "balance":"0",
            "last":"2019-04-01T14:21:00.8344529+08:00",
            "decimals":"9",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/B99.png",
            "legalValue":"0",
            "isToken":true,
            "idx":1,
            "feeInfo":null
        }
     ]
}
```

### sdk_getAssets

#### 请求格式

参数
| 字段名     | 类型   | 必须 | 说明     |
| ---------- | ------ | ---- | -------- |
| walletAddr | string | 是   | 钱包地址 |

请求示例

```json
{
    "method": "sdk_getAssets",
    "params": {
        "walletAddr": "bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9"
    }
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result":[
        {
            "id":4,
            "cid":2,
            "coinType":"0x1001",
            "chainType":1,
            "chainName":"BCB链",
            "name":"BCBT",
            "name_customer":"BCBT",
            "symbol":"BCBT",
            "symbol_customer":"BCBT",
            "decimals":"9",
            "conAddr":"bcbtestAtEJ4dTejwJReKA4dtFjy9cQ3HzR6jbwF",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/BCBMainNet.png",
            "config":1,
            "idx":0,
            "appid":"1",
            "modifyTime":"2018-09-29T13:21:10"
        },
        {
            "id":3,
            "cid":4,
            "coinType":"0x1001",
            "chainType":1,
            "chainName":"BCB链",
            "name":"B99",
            "name_customer":"B99",
            "symbol":"B99",
            "symbol_customer":"B99",
            "decimals":"9",
            "conAddr":"bcbtestDhxdEq9JPFhQ8xicUdSAHQHxymP2orXYW",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/B99.png",
            "config":1,
            "idx":1,
            "appid":"1",
            "modifyTime":"2018-09-29T11:51:06"
        }
    ]
}
```

### sdk_getCoinDeatil

#### 请求格式
参数

| 字段名      | 类型   | 必须 | 说明                                               |
| ----------- | ------ | ---- | -------------------------------------------------- |
| walletAddr  | string | 是   | 钱包地址                                           |
| conAddr     | string | 是   | 币种合约地址                                       |
| legalSymbol | string | 是   | 币种资产的法币计价单位，人民币为：CNY；美元为：USD |

请求示例
```json
{
	"method": "sdk_getCoinDeatil",
	"params": {
		"walletAddr": "bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9",
        "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "legalSymbol":"CNY"
	}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result":{
        "addr":"bcbESMNFs8Cekc9H6xQcu3a2p4NvJDtNoy8S",
        "coinType":"0x1002",
        "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "name":"BCB",
        "symbol":"BCB",
        "balance":"4.99905",
        "last":"2019-04-01T14:44:20.4735693+08:00",
        "decimals":"9",
        "coinIcon":"https://www.n8.app/public/resource/coin/icon/BCBMainNet.png",
        "legalValue":"215.21092615344",
        "isToken":false,
        "idx":65535,
        "feeInfo":{
            "id":1,
            "isUniteCoin":false,
            "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            "percent":0,
            "maxfee":null,
            "minfee":null,
            "feeName":null,
            "bcbFee":"0.00125",
            "modifyTime":"2018-11-01T08:56:40"
        }
    }
}
```

### sdk_getCoinTransactionDetail

#### 请求格式
参数
| 字段名     | 类型   | 必须 | 说明         |
| ---------- | ------ | ---- | ------------ |
| walletAddr | string | 是   | 钱包地址     |
| conAddr    | string | 是   | 币种合约地址 |
| page       | int    | 是   | 页码从0开始  |
| count      | int    | 是   | 条数         |

请求示例

```json
{
	"method": "sdk_getCoinTransactionDetail",
	"params": {
		"walletAddr": "bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9",
        "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "page":1,
        "count":20
	}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result":{
        "records":[
            {
                "id":12858549,
                "coinType":"0x1002",
                "from":"bcb2kerqmq8ZRPneB4mp2Qv4qSwDyhtLYwb8",
                "to":"bcbESMNFs8Cekc9H6xQcu3a2p4NvJDtNoy8S",
                "conAddr":"bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ",
                "value":"175.756694",
                "valueName":"DC",
                "fee":"0.0015",
                "feeName":"BCB",
                "timeStamp":"1553238936",
                "blockN":"9603760",
                "source":null,
                "txHash":"D67097C9E342213B7F46C8D680C96099907A81096E975847D7C204CDA76CAD70",
                "memo":"BalancePo CoinTransfer:1553238925228RK7EwEBSC1KO",
                "status":"0x1",
                "balanceFromFlag":0,
                "balanceToFlag":0,
                "pushFromCnt":0,
                "modifyTime":"2019-03-22T15:15:37"
            }
        ]
    } 
}
```

### sdk_encryptContent

数据加密

#### 请求格式

参数

| name    | type   | required | description |
| :------ | :----- | :------- | :---------- |
| content | string | yes      | 加密内容    |

请求示例

```json
{
    "method": "sdk_encryptContent",
    "params": {
        "content":"test",
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
	"msg": "ok",
	"result": "/suzXLeVk3tU3AmFe1/lhA=="
}
```

### sdk_decryptContent

数据解密

#### 请求格式

参数

| name    | type   | required | description |
| :------ | :----- | :------- | :---------- |
| content | string | yes      | 解密内容    |

请求示例

```json
{
    "method": "sdk_decryptContent",
    "params": {
        "content":"/suzXLeVk3tU3AmFe1/lhA==",
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"ok",
	"result": "test"
}
```

### sdk_genKeyPair

生成密钥对

请求示例

```json
{
    "method": "sdk_genKeyPair",
    "params": {}
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"ok",
	"result": {
		"mnemonic": "step easy argue casual one hour engage excite speak slab detail blossom",
		"priKey": "29DA5671048493912669E3F309DFE8D1703CD2DB11AC15B973E6035A4D153D1F",
		"pubKey": "46BD93A849ACA46F3B51728C36DE40BC27A15B3760B89243DEE624B92A1BB681"
	}
}
```

### sdk_genericSign

私钥签名

#### 请求格式

参数

| name   | type   | required | description   |
| :----- | :----- | :------- | :------------ |
| priKey | string | yes      | 私钥hex       |
| data   | string | yes      | 待签名内容hex |

请求示例

```json
{
    "method": "sdk_genericSign",
    "params": {
        "priKey":"29DA5671048493912669E3F309DFE8D1703CD2DB11AC15B973E6035A4D153D1F",
        "data":"E8C0B40BE53F9869D8E51B830936C131112083DC746"
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"ok",
	"result": {
		"pubKey": "4C24B251B0A1FEDCE66DDD37A3CBC4FC46B5173A201BBC840A98FB5F29C496F3",
		"signature": "E8C0B40BE53F9869D8E51B830936C131112083DC746CCE16AA3BF002D24A8B16A0CEDA79EF803B39CF8D7539E0C685DEA47CBE2524B7F8D36590816928559908"
	}
}
```

### sdk_verifySign

数据验签

#### 请求格式

参数

| name      | type   | required | description             |
| :-------- | :----- | :------- | :---------------------- |
| type      | string | yes      | 算法，目前只支持ed25519 |
| data      | string | 是       | 待验签内容（hexstring） |
| pubKey    | string | 是       | 验签公钥（hexstring）   |
| signature | string | 是       | 签名（hexstring）       |

请求示例

```json
{
    "method": "sdk_verifySign",
    "params": {
        "type":"ed25519",
        "data":"",
        "pubKey":"",
        "signature":""
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
	"msg": "success",
	"result": ""
}
```

### sdk_getAddrFromMnemonicWords

根据助记词返回钱包地址

#### 请求格式

参数

| name          | type   | required | description |
| :------------ | :----- | :------- | :---------- |
| mnemonicWords | string | yes      | 助记词      |

请求示例

```json
{
    "method": "sdk_getAddrFromMnemonicWords",
    "params": {
        "mnemonicWords":"eyebrow indoor orbit cinnamon hour gain category spawn walk bind spread clinic",
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"",
	"result": {
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
    }
}
```

### sdk_getAddrFromPrivateKey

根据私钥返回钱包地址

#### 请求格式

参数

| name       | type   | required | description |
| :--------- | :----- | :------- | :---------- |
| privateKey | string | yes      | 私钥        |

请求示例

```json
{
    "method": "sdk_getAddrFromPrivateKey",
    "params": {
        "privateKey":"0x98BB2E49822A48728E3CBCFD1A933C1FC500A6204453E7DB85F84EFB90146600",
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"",
	"result": {
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
    }
}
```

### sdk_getAddrFromKeystore

根据Keystore返回钱包地址

#### 请求格式

参数

| name     | type   | required | description |
| :------- | :----- | :------- | :---------- |
| keystore | string | yes      | keystore    |
| password | string | yes      | 密码        |

请求示例

```json
{
    "method": "sdk_getAddrFromKeystore",
    "params": {
        "keystore":".......",
        "password":"qwer1234"
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"",
	"result": {
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
    }

```



# 新增云钱包接口

### sdk_setCloudDomain

初始化域名设置

#### 请求格式

参数

| name   | type   | required | description |
| :----- | :----- | :------- | :---------- |
| domain | string | yes      | 域名        |

请求示例

```json
{
	"method": "sdk_setCloudDomain",
	"params": {
		"domain": "https://api.iwallet.cloud/pkey_api"
	}
}
```

返回示例

```json
{
    "code":0,
    "msg":"ok",
	"result": {}
}
```

### 

### sdk_setCloudMerchantId

初始化设置

#### 请求格式

参数

| name           | type   | required | description  |
| :------------- | :----- | :------- | :----------- |
| merchantId     | string | yes      | 商户ID       |
| remoteDHPubKey | string | yes      | 商户对应公钥 |

请求示例

```json
{
	"method": "sdk_setCloudMerchantId",
	"params": {
		"merchantId": "4fdc8f51ac084d3b9c2a749a0280a081",
        "remoteDHPubKey":"cf06693d7061dcd2d03cb27d4effbdbd6d5257a74574e456447f47b5e4024126"
	}
}
```

返回示例

```json
{
    "code":0,
    "msg":"ok",
	"result": {}
}
```

### sdk_getCloudCode

获取验证码

#### 请求格式

参数

| name    | type   | required | description                              |
| :------ | :----- | :------- | :--------------------------------------- |
| account | string | yes      | 手机号(+86139****)或邮箱（12345@qq.com） |

请求示例

```json
{
    "method": "sdk_getCloudCode",
    "params": {
        "account":"+86139***"
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"ok",
	"result": {}

```

### sdk_bindAccount

绑定账号

#### 请求格式

参数

| name    | type   | required | description                              |
| :------ | :----- | :------- | :--------------------------------------- |
| account | string | yes      | 手机号(+86139****)或邮箱（12345@qq.com） |
| code    | string | yes      | 验证码                                   |

请求示例

```json
{
    "method": "sdk_bindAccount",
    "params": {
        "account":"+86138...",
        "code":"123123"
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"ok",
	"result": {}

```

### sdk_createCloudWallet

创建云钱包地址

#### 请求格式

参数

| name      | type   | required | description             |
| :-------- | :----- | :------- | :---------------------- |
| chainType | string | yes      | 主链（目前只支持BCB链） |

请求示例

```json
{
    "method": "sdk_createCloudWallet",
    "params": {
        "chainType":"BCB"
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"ok",
    "result": {
        "address":"bcbAaKWWE3botCiuXMj58d8TPX56dvUk3wj1"
    }

```

### sdk_getCloudWalletList

获取云钱包地址列表

#### 请求格式

参数

| name      | type   | required | description             |
| :-------- | :----- | :------- | :---------------------- |
| chainType | string | yes      | 主链（目前只支持BCB链） |

请求示例

```json
{
    "method": "sdk_getCloudWalletList",
    "params": {
        "chainType":"BCB"
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"ok",
    "result": [
        "bcbAaKWWE3botCiuXMj58d8TPX56dvUk3wj1",
        "bcbAaKWWE3botCiuXMj58d8TPX56dvUk3wj1"
    ]

```

### sdk_cloudWalletTransation

云钱包支付

#### 请求格式

参数

| name       | type   | required | description                                                  |
| :--------- | :----- | :------- | :----------------------------------------------------------- |
| walletAddr | string | yes      | 钱包地址                                                     |
| chainType  | string | yes      | 主链（目前只支持BCB链）                                      |
| walletCall | string | yes      | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |

请求示例

```json
{
    "method": "sdk_cloudWalletTransation",
    "params": {
        "walletAddr":"bcbAaKWWE3botCiuXMj58d8TPX56dvUk3wj1",
        "chainType":"BCB",
        "walletCall":"{\"note\":\"request-banker\",\"gasLimit\":\"3500000\",\"calls\":[{\"contract\":\"bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ\",\"method\":\"Transfer(types.Address,bn.Number)\",\"params\":[\"bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH\",\"10\"]}]}"
    }
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
    "msg":"ok",
    "result": {
        "txHash":"0x0F8642968E48A16316CD499BF142E15EEFF03BE44816796AF87DDC2F1B72BBA4"
    }

```

### sdk_getCloudAddrsBalance

获取云钱包地址余额

#### 请求格式

参数

| 字段名      | 类型   | 必须 | 说明                                           |
| ----------- | ------ | ---- | ---------------------------------------------- |
| walletAddr  | string | 是   | 钱包地址                                       |
| legalSymbol | string | 是   | 资产的法币计价单位，人民币为：CNY；美元为：USD |

#### 请求示例

```json
{
	"method": "sdk_getCloudAddrsBalance",
	"params": {
		"walletAddr": "bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9",
		"legalSymbol": "CNY"
	}
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
	"msg": "ok",
	"result":[
        {
            "addr":"bcbtestCTLvcA7pa1RqCncL2fRcALgRrVYudJNeE",
            "coinType":"0x1001",
            "conAddr":"bcbtestAtEJ4dTejwJReKA4dtFjy9cQ3HzR6jbwF",
            "name":"BCBT",
            "symbol":"BCBT",
            "balance":"101",
            "last":"2019-04-01T14:21:00.8342387+08:00",
            "decimals":"9",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/BCBMainNet.png",
            "legalValue":"688.8604",
            "isToken":false,
            "idx":0,
            "feeInfo":null
        },
        {
            "addr":"bcbtestCTLvcA7pa1RqCncL2fRcALgRrVYudJNeE",
            "coinType":"0x1001",
            "conAddr":"bcbtestDhxdEq9JPFhQ8xicUdSAHQHxymP2orXYW",
            "name":"B99",
            "symbol":"B99",
            "balance":"0",
            "last":"2019-04-01T14:21:00.8344529+08:00",
            "decimals":"9",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/B99.png",
            "legalValue":"0",
            "isToken":true,
            "idx":1,
            "feeInfo":null
        }
     ]
}
```

### sdk_getCloudCoinDeatil

获取云钱包指定地址、指定币种信息

#### 请求格式

参数

| 字段名      | 类型   | 必须 | 说明                                               |
| ----------- | ------ | ---- | -------------------------------------------------- |
| walletAddr  | string | 是   | 钱包地址                                           |
| conAddr     | string | 是   | 币种合约地址                                       |
| legalSymbol | string | 是   | 币种资产的法币计价单位，人民币为：CNY；美元为：USD |

请求示例

```json
{
	"method": "sdk_getCloudCoinDeatil",
	"params": {
		"walletAddr": "bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9",
        "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "legalSymbol":"CNY"
	}
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
	"msg": "ok",
	"result":{
        "addr":"bcbESMNFs8Cekc9H6xQcu3a2p4NvJDtNoy8S",
        "coinType":"0x1002",
        "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "name":"BCB",
        "symbol":"BCB",
        "balance":"4.99905",
        "last":"2019-04-01T14:44:20.4735693+08:00",
        "decimals":"9",
        "coinIcon":"https://www.n8.app/public/resource/coin/icon/BCBMainNet.png",
        "legalValue":"215.21092615344",
        "isToken":false,
        "idx":65535,
        "feeInfo":{
            "id":1,
            "isUniteCoin":false,
            "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            "percent":0,
            "maxfee":null,
            "minfee":null,
            "feeName":null,
            "bcbFee":"0.00125",
            "modifyTime":"2018-11-01T08:56:40"
        }
    }
}
```

### sdk_getCloudCoinTransactionDetail

获取云钱包地址交易记录

#### 请求格式

参数

| 字段名     | 类型   | 必须 | 说明         |
| ---------- | ------ | ---- | ------------ |
| walletAddr | string | 是   | 钱包地址     |
| conAddr    | string | 是   | 币种合约地址 |
| page       | int    | 是   | 页码从0开始  |
| count      | int    | 是   | 条数         |

请求示例

```json
{
	"method": "sdk_getCloudCoinTransactionDetail",
	"params": {
		"walletAddr": "bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9",
        "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "page":0,
        "count":20
	}
}
```

#### 返回格式

返回示例

```json
{
    "code":0,
	"msg": "ok",
	"result":{
        "records":[
            {
                "id":12858549,
                "coinType":"0x1002",
                "from":"bcb2kerqmq8ZRPneB4mp2Qv4qSwDyhtLYwb8",
                "to":"bcbESMNFs8Cekc9H6xQcu3a2p4NvJDtNoy8S",
                "conAddr":"bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ",
                "value":"175.756694",
                "valueName":"DC",
                "fee":"0.0015",
                "feeName":"BCB",
                "timeStamp":"1553238936",
                "blockN":"9603760",
                "source":null,
                "txHash":"D67097C9E342213B7F46C8D680C96099907A81096E975847D7C204CDA76CAD70",
                "memo":"BalancePo CoinTransfer:1553238925228RK7EwEBSC1KO",
                "status":"0x1",
                "balanceFromFlag":0,
                "balanceToFlag":0,
                "pushFromCnt":0,
                "modifyTime":"2019-03-22T15:15:37"
            }
        ]
    } 
}
```

### 