## API

### sdk_setWalletModel

设置开发环境

#### 请求格式

参数

| name        | type | required | description                                         |
| :---------- | :--- | :------- | :-------------------------------------------------- |
| walletModel | int  | yes      | 钱包管理链环境（*0：测试链、1：正式链、2：研发链*） |

请求示例

```json
{
	"method": "sdk_setWalletModel",
	"params": {
		"walletModel": 0,
	},
}
```

返回示例

```json
ok
```

### sdk_getChainInfo

获取当前环境所有链的信息

#### 请求格式

请求示例

```json
{
	"method": "sdk_getChainInfo",
	"params": {}
}
```

#### 返回格式

返回示例

```json
["bcb","yy","jiuj"]
```

###  sdk_switchChain

切换链

#### 请求格式

请求示例
```json
{
	"method": "sdk_switchChain",
	"params": {
		"chainName": "bcb"
	}
}
```

#### 返回格式

返回示例

```json
bcb
```

### sdk_getCurrentChain

获取当前链的名称

#### 请求格式

请求示例
```json
{
	"method": "sdk_getCurrentChain",
	"params": {}
}
```

#### 返回格式

返回示例

```json
bcb
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

| name   | type   | required | description        |
| :----- | :----- | :------- | :----------------- |
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
		"name": "myWall",
		"password": "1234qwer",
		"recommend": ""
	}
}
```

#### 返回格式
返回示例
```json
{
    "address": "bcbgcbRe6qkyW43LcoNaGq3iP685xskCsmi",
    "name": "myWall",
    "mnemonicWords": "0xC5AE4BA707904F08CA8AC4D8AA6A1D69D51717E5AE6A49A9DB5B4F11E0405CAC66BC54E296786B505E7AC1AEA2F076B142288FB485EB07A37CD18FF58D09ED31CAC31FA688E110708E8FE81401A58272"
}
```


### sdk_importPrivateKey
导入私钥生成钱包

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| name      | string | 是       | 钱包名称         |
| privatekey | string | 是       | 私钥             |
| password  | string | 是       | 钱包密码         |
| recommend | string | 否       | 推荐人的钱包地址 |

请求示例
```json
{
	"method": "sdk_importPrivateKey",
	"params": {
		"name": "myWallet",
		"privatekey": "0x7E85A051FA133EDD5F48377479608DAB8DF0BCC17EC838924ED7EABC4539770F",
		"password": "1234qwer",
		"recommend": ""
	}
}
```

#### 返回格式
返回示例
```json
{
    "importType": 1,
    "address": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
    "name": "myWallet"
}
```

### sdk_importKeystore
导入Keystore生成钱包

#### 请求格式
参数
| name       | type   | required | description      |
| :--------- | :----- | :------- | :--------------- |
| name       | string | 是       | 钱包名称         |
| privatekey | string | 是       | Keystore         |
| password   | string | 是       | 钱包密码         |
| recommend  | string | 否       | 推荐人的钱包地址 |

请求示例

```json
{
	"method": "sdk_importKeystore",
	"params": {
		"name": "myWallet",
		"privatekey":"{\"address\":\"bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX\",\"crypto\":{\"cipher\":\"aes-128-ctr\",\"cipherparams\":{\"iv\":\"94fac2ff66f9931121000cce5f72463a\"},\"ciphertext\":\"8cc57ffc30d38345279afb2c84a3f2a9218c4f76e9f32ab1a6afa27d68beeaa3\",\"kdf\":\"scrypt\",\"kdfparams\":{\"dklen\":32,\"n\":65536,\"p\":8,\"r\":1,\"salt\":\"b0244994a205bcf84f01610a8470b7f4c6ab004d217aea211471bf327e813b6e\"},\"mac\":\"291c31d454564aaec12476f238bd5dc0b20189b702db4164801b870bc34a7b16\"},\"id\":\"ba41fe85-c6f6-ed57-1c46-3e1abf56b873\",\"version\":3}",
		"password": "1234qwer",
		"recommend": ""
	}
}
```

#### 返回格式
返回示例
```json
{
    "importType": 2,
    "address": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
    "name": "myWallet"
}
```

### sdk_importMnemonicWords
导入助记词生成钱包

#### 请求格式
参数

| name       | type   | required | description      |
| :--------- | :----- | :------- | :--------------- |
| name       | string | 是       | 钱包名称         |
| privatekey | string | 是       | 助记词           |
| password   | string | 是       | 钱包密码         |
| recommend  | string | 否       | 推荐人的钱包地址 |

请求示例

```json
{
	"method": "sdk_importMnemonicWords",
	"params": {
		"name": "myWallet2",
		"privatekey": "visa bid impact amused exile cousin satisfy phone ghost surge sentence girl",
		"password": "1234qwer",
		"recommend": ""
	}
}
```

#### 返回格式
返回示例
```json
{
    "importType": 3,
    "address": "bcbgcbRe6qkyW43LcoNaGq3iP685xskCsmi",
    "name": "myWallet2"
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
[
    {
        "importType": 2,
        "address": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "name": "新钱包"
    }
]
```
###  sdk_exportMnemonicWords

导出助记词

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| address | string     | yes        | 钱包地址      |
| password | string | yes | 钱包密码 |

请求示例
```json
{
	"method": "sdk_exportMnemonicWords",
	"params": {
		"address": "bcbgcbRe6qkyW43LcoNaGq3iP685xskCsmi",
		"password": "1234qwer"
	}
}
```

#### 返回格式
返回示例
```json
visa bid impact amused exile cousin satisfy phone ghost surge sentence girl
```

### sdk_exportPrivateKey
导出私钥

#### 请求格式
参数
| name     | type   | required | description |
| :------- | :----- | :------- | :---------- |
| address  | string | yes      | 钱包地址    |
| password | string | yes      | 钱包密码    |

请求示例

```json
{
	"method": "sdk_exportPrivateKey",
	"params": {
		"address":"bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
		"password": "1234qwer"
		}
}
```

#### 返回格式
返回示例
```json
0x27939421C7662DA744063AB409534A4B36F75741A45134BEE80FB9D3BE769DAA
```

### sdk_exportKeystore
导出Keystore

#### 请求格式
参数
| name     | type   | required | description |
| :------- | :----- | :------- | :---------- |
| address  | string | yes      | 钱包地址    |
| password | string | yes      | 钱包密码    |

请求示例

```json
{
    "method": "sdk_exportKeystore",
    "params": {
        "address":"bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "password":"1234qwer"
    }
}
```

#### 返回格式
返回示例
```json
{"address":"bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX","crypto":{"cipher":"aes-128-ctr","cipherparams":{"iv":"8701cdb61264d0409925f37d7caf9523"},"ciphertext":"63bb0d821d551dc8762e270579795d247b45ebd49a52d5c779eae126497d6fb2","kdf":"scrypt","kdfparams":{"dklen":32,"n":65536,"p":8,"r":1,"salt":"11f84f631e0f4cc96c5e7f48ef234856a34b99b7ca49b6d4b34bdb6471a7b150"},"mac":"efc136aa4ee13fb6d0c770f484ec0ba8e7a70c07c832276453f28086519e09b2"},"id":"087d28ac-6064-f50d-19a0-c7b5e1a2e12d","version":3}
```

### sdk_verifyPassword
验证钱包密码

#### 请求格式
参数
| name     | type   | required | description |
| :------- | :----- | :------- | :---------- |
| address  | string | yes      | 钱包地址    |
| password | string | yes      | 钱包密码    |

请求示例

```json
{
    "method": "sdk_verifyPassword",
    "params": {
        "address":"bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "password":"1234qwer"
    }
}
```

#### 返回格式
返回示例
```json
true
```

### sdk_changePassword
修改钱包密码

#### 请求格式
参数
| name        | type   | required | description |
| :---------- | :----- | :------- | :---------- |
| address     | string | yes      | 钱包地址    |
| oldPassword | string | yes      | 原钱包密码  |
| newPassword | string | yes      | 新钱包密码  |

请求示例

```json
{
    "method": "sdk_changePassword",
    "params": {
        "address":"bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "oldPassword":"1234qwer",
        "newPassword":"1234qwerrrrr"
    }
}
```

#### 返回格式
返回示例
```json
true
```

### sdk_changeWalletName
修改钱包名称

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| address | string     | yes        | 钱包地址 |
| newName | string     | yes        | 新钱包地址 |

请求示例
```json
{
    "method": "sdk_changeWalletName",
    "params": {
        "address":"bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "newName":"netwallet"
    }
}
```

#### 返回格式
返回示例
```json
true
```

### sdk_deleteWallet
删除钱包

#### 请求格式
参数
| name     | type   | required | description |
| :------- | :----- | :------- | :---------- |
| address  | string | yes      | 钱包地址    |
| password | string | yes      | 钱包密码    |

请求示例

```json
{
    "method": "sdk_deleteWallet",
    "params": {
        "address":"bcbgcbRe6qkyW43LcoNaGq3iP685xskCsmi",
        "password":"1234qwer"
    }
}
```

#### 返回格式
返回示例
```json
true
```

### sdk_walletTransaction
钱包转账

#### 请求格式
参数
| 字段名   | 类型   | 必须 | 说明                                              |
| -------- | ------ | ---- | ------------------------------------------------- |
| address  | string | 是   | 钱包地址                                          |
| password | string | 是   | 钱包密码                                          |
| coinAddr | string | 是   | 要转账币种的合约地址                              |
| toAddr   | string | 是   | 转账到的目标地址                                  |
| value    | string | 是   | 转账的金额，例如"102.23"                          |
| note     | string | 否   | 转账的备注，对于BCB链，这个字段最终会写入到区块中 |

#### 请求示例

```json
{
	"method": "sdk_walletTransaction",
	"params": {
		"address": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
		"password": "1234qwer",
		"coinAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
		"toAddr": "bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH",
		"value": "0.0001",
	}
}
```

#### 返回格式
结果
- txHash：交易hash

返回示例
```json
24A7F87C838DE883B91AC67C24ADF84FAAC934184AF706679C1675A5735B9BFB
```

### sdk_walletCommonPay

#### 请求格式
参数
| 字段名     | 类型   | 必须 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| address    | string | 是   | 钱包地址                                                     |
| version    | Int    | 是   | 1.0的支付传1， 2.0的支付传2   3.0的支付传3                   |
| password   | string | 是   | 钱包密码                                                     |
| walletCall | string | 是   | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |

**示例：walletCall字符串格式**

```java
"{\"walletCall\":{\"conAddr\":\"bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9\",\"methodName\":\"BuyXid\",\"methodParam\":[{\"name\":\"_affCode\",\"type\":\"int64\",\"value\":\"12345678\"},{\"name\":\"_team\",\"type\":\"int64\",\"value\":\"0\"},{\"name\":\"_bcb\",\"type\":\"Number-decimal\",\"value\":\"2.5\"}],\"methodRet\":\"smc.Error\"}}"
```

请求示例

```json
{
	"method": "sdk_walletCommonPay",
	"params": {
		"address": "bcbhl1n2mdjpasnf3n6csx77ukwe2wsh5tux",
		"version": 2,
		"password": "1234qwer",
		"walletCall": "{\"note\":\"ApplyToBanker\",\"gasLimit\":\"3500000\",\"contractCall\":[{\"contractAddr\":\"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe\",\"methodName\":\"Transfer\",\"methodParams\":[{\"type\":\"types.Address\",\"value\":\"bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH\"},{\"type\":\"bn.Number-decimal\",\"value\":\"0.0001\"}],\"methodRet\":\"\"}]}"
	}
}
```

#### 返回格式
```json
24A7F87C838DE883B91AC67C24ADF84FAAC934184AF706679C1675A5735B9BFB
```

### sdk_getAddrBalance

#### 请求格式

参数
| 字段名      | 类型   | 必须 | 说明                                           |
| ----------- | ------ | ---- | ---------------------------------------------- |
| address     | string | 是   | 钱包地址                                       |
| legalSymbol | string | 是   | 资产的法币计价单位，人民币为：CNY；美元为：USD |

#### 请求示例

```json
{
	"method": "sdk_getAddrBalance",
	"params": {
		"address": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
		"legalSymbol": "USD"
	}
}
```

#### 返回格式
结果
- txHash：交易hash

返回示例
```json
[
    {
        "isToken": "true",
        "symbol": "DC",
        "conAddr": "bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ",
        "balance": "1.9399",
        "decimals": "9",
        "name": "Diamond Coin",
        "addr": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "legalValue": "0.27662974",
        "coinIcon": "https:\/\/bcbpushsrv.bcbchain.io\/public\/resource\/coin\/icon\/ecdba0e2f6615760b196edd49a2f1bf0.png"
    },
    {
        "isToken": "false",
        "symbol": "BCB",
        "conAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "balance": "0.650358799",
        "decimals": "9",
        "name": "BCB",
        "addr": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "legalValue": "4.001657690247",
        "coinIcon": "https:\/\/bcbpushsrv.bcbchain.io\/public\/resource\/coin\/icon\/fae8dd88927ea0ca872a889681cd2902.png"
    }
]
```

### sdk_getAssets

#### 请求格式

参数
| 字段名  | 类型   | 必须 | 说明     |
| ------- | ------ | ---- | -------- |
| address | string | 是   | 钱包地址 |

请求示例

```json
{
    "method": "sdk_getAssets",
    "params": {
        "address": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX"
    }
}
```

#### 返回格式
返回示例
```json
[
    {
        "coinType": "0x1002",
        "symbol": "DC",
        "conAddr": "bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ",
        "balance": "1.9399",
        "decimals": "9",
        "name": "Diamond Coin",
        "legalValue": "1.9399",
        "coinIcon": "https:\/\/bcbpushsrv.bcbchain.io\/public\/resource\/coin\/icon\/ecdba0e2f6615760b196edd49a2f1bf0.png"
    },
    {
        "coinType": "0x1002",
        "symbol": "BCB",
        "conAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "balance": "0.650358799",
        "decimals": "9",
        "name": "BCB",
        "legalValue": "28.0512803245513",
        "coinIcon": "https:\/\/bcbpushsrv.bcbchain.io\/public\/resource\/coin\/icon\/fae8dd88927ea0ca872a889681cd2902.png"
    }
]
```

### sdk_getCoinDetail

#### 请求格式
参数

| 字段名      | 类型   | 必须 | 说明                                               |
| ----------- | ------ | ---- | -------------------------------------------------- |
| address     | string | 是   | 钱包地址                                           |
| conAddr     | string | 是   | 币种合约地址                                       |
| legalSymbol | string | 是   | 币种资产的法币计价单位，人民币为：CNY；美元为：USD |

请求示例
```json
{
	"method": "sdk_getCoinDetail",
	"params": {
		"address": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "legalSymbol":"CNY"
	}
}
```

#### 返回格式
返回示例
```json
{
    "symbol": "BCB",
    "conAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
    "balance": "0.650358799",
    "fee": "0.00125",
    "name": "BCB",
    "addr": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
    "legalValue": "28.0512803245513",
    "coinIcon": "https:\/\/bcbpushsrv.bcbchain.io\/public\/resource\/coin\/icon\/fae8dd88927ea0ca872a889681cd2902.png"
}
```

### sdk_getCoinTransactionDetail

#### 请求格式
参数
| 字段名     | 类型   | 必须 | 说明         |
| ---------- | ------ | ---- | ------------ |
| walletAddr | string | 是   | 钱包地址     |
| conAddr    | string | 是   | 币种合约地址 |
| page       | int    | 是   | 页码从1开始  |
| count      | int    | 是   | 条数         |

请求示例

```json
{
	"method": "sdk_getCoinTransactionDetail",
	"params": {
		"walletAddr": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
		"conAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
		"page": 1,
		"count": 20
	}
}
```

#### 返回格式
返回示例
```json
[
    {
        "blockN": "27035137",
        "valueName": "BCB",
        "fee": "0.005",
        "memo": "ApplyToBanker",
        "timeStamp": "1574254648",
        "conAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "modifyTime": "2019-11-20T20:57:29",
        "feeName": "BCB",
        "from": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "to": "bcb[yy]KyoEZEr7JkDZwXR7DdEaLqTCJVeqjjT13",
        "txHash": "A6936684558F39F795BBC79067FC2B47A4319C5CE2ED526F3203986F89538BB7",
        "value": "0.0001",
        "status": "0x1"
    },
    {
        "blockN": "27035060",
        "valueName": "BCB",
        "fee": "0.00125",
        "memo": "ApplyToBanker",
        "timeStamp": "1574254530",
        "conAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "modifyTime": "2019-11-20T20:55:32",
        "feeName": "BCB",
        "from": "bcbHL1n2mDJPasnF3n6Csx77UKWE2WSh5TuX",
        "to": "bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH",
        "txHash": "24A7F87C838DE883B91AC67C24ADF84FAAC934184AF706679C1675A5735B9BFB",
        "value": "0.0001",
        "status": "0x1"
    }
]
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
/suzXLeVk3tU3AmFe1/lhA==
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
test
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
    "mnemonic": "step easy argue casual one hour engage excite speak slab detail blossom",
	"priKey": "29DA5671048493912669E3F309DFE8D1703CD2DB11AC15B973E6035A4D153D1F",
	"pubKey": "46BD93A849ACA46F3B51728C36DE40BC27A15B3760B89243DEE624B92A1BB681"
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
   "pubKey": "4C24B251B0A1FEDCE66DDD37A3CBC4FC46B5173A201BBC840A98FB5F29C496F3",
	"signature": "E8C0B40BE53F9869D8E51B830936C131112083DC746CCE16AA3BF002D24A8B16A0CEDA79EF803B39CF8D7539E0C685DEA47CBE2524B7F8D36590816928559908"
}
```

### sdk_verifySign

数据验签

#### 请求格式

参数

| name      | type   | required | description             |
| :-------- | :----- | :------- | :---------------------- |
| content   | string | 是       | 待验签内容（hexstring） |
| pubKey    | string | 是       | 验签公钥（hexstring）   |
| signature | string | 是       | 签名（hexstring）       |

请求示例

```json
{
    "method": "sdk_verifySign",
    "params": {
        "content":"",
        "pubKey":"",
        "signature":""
    }
}
```

#### 返回格式

返回示例

```json
true
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
bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5
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
bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5
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
bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5
```

