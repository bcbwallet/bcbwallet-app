## API

### sdk_regist

初始化注册应用

#### 请求格式

参数

| name   | type   | required | description |
| :----- | :----- | :------- | :---------- |
| appId  | string | yes      | 应用ID      |
| apiKey | string | yes      | 托管私钥    |
| domain | string | yes      | 域名地址    |

请求示例

```json
{
	"method": "sdk_regist",
	"params": {
		"appId": "d00a0ee91c82493587c1f8fcbece227b",
        "apiKey":"4cff994515c0543ddc8cf6d4f59f2c8ee09414e51831f941322ddf50b4576b60",
        "domain":"https://tcapi.ikey.cloud"
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

###  sdk_setChainType

设置链类型

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| chainType | string     | yes        | 如：BCB、BCBT.... |

请求示例
```json
{
	"method": "sdk_setChainType",
	"params": {
		"chainType": "BCB",
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

### sdk_loggedAccount

获取当前登录账户

请求示例
```json
{
	"method": "sdk_loggedAccount",
	"params": {},
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

### sdk_getCode

获取验证码 

#### 请求格式

参数

| name    | type   | required | description                                 |
| :------ | :----- | :------- | :------------------------------------------ |
| account | string | yes      | 账户（手机号：+86139\****或邮箱123@qq.com） |

请求示例
```json
{
	"method": "sdk_getCode",
    "params": {
        "account":"123@qq.com"
    }
}
```

返回示例
```json
{
    "code":0,
	"msg": "ok"
}
```

### sdk_walletLogin
登录

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| account | string | yes      | 账户（手机号：+86139\****或邮箱123@qq.com） |
| code    | string | yes      | 验证码                                      |

请求示例
```json
{
	"method": "sdk_walletLogin",
	"params": {
		"account": "123@qq.com",
        "code":"123456"
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

### sdk_addVerify
添加二次验证

#### 请求格式

参数

| name        | type   | required | description                                       |
| :---------- | :----- | :------- | :------------------------------------------------ |
| account     | string | yes      | 新添加号码（手机号：+86139\****或邮箱123@qq.com） |
| accountCode | string | yes      | 新号码验证码                                      |
| verifyCode  | string | yes      | 老号码验证码                                      |

请求示例
```json
{
	"method": "sdk_addVerify",
    "params": {
        "account": "1234@qq.com",
        "accountCode":"123456",
        "verifyCode":"111111"
    }
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok"
}
```

### sdk_getUserInfo
域名设置

#### 请求格式
请求示例
```json
{
    "method": "sdk_getUserInfo",
	"params": {}
}
```

#### 返回格式
```json
{
    "code":0,
    "msg":"ok",
    "result": {
        "userName": "",
        "memo": "",
        "phone": "",
        "email": "",
        "hasPWD": false,
        "createTime": "",
        "lastTime": ""
    }
}
```

### sdk_setWalletPayPwd
设置钱包密码

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| password  | string | 是       | 钱包密码         |
| code | string | 否       | 初次设置密码时可传空字符串 |

请求示例
```json
{
	"method": "sdk_setWalletPayPwd",
	"params": {
		"password": "qwer1234",
		"code": ""
	}
}
```

#### 返回格式
返回示例
```json
{
  "msg" : "ok",
  "code" : 0
}
```


### sdk_updateWalletPayPwd
修改钱包支付密码

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| oldPwd | string | 是       | 老钱包密码        |
| newPwd | string | 是   | 新钱包密码 |

请求示例
```json
{
	"method": "sdk_updateWalletPayPwd",
	"params": {
		"oldPwd": "123456",
		"newPwd": "111111"，
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

### sdk_createCloudWallet
创建托管钱包

#### 请求格式
请求示例

```json
{
	"method": "sdk_createCloudWallet",
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
	{	
        "address":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
	}
}
```

### sdk_getCloudWalletList
获取托管钱包列表

#### 请求格式
请求示例

```json
{
	"method": "sdk_getCloudWalletList",
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
		"bcbH8EnQ12jEeTXzPWKByVidjmaGXSTbHn3T",
        "bcbFdDBN2k3Xs6dp4FfwLCy9cMPGjNusGNxT"
	]
}
```

### sdk_cloudWalletTransaction
构造并签名交易

#### 请求格式

参数

| name       | type   | required | description                                                  |
| ---------- | ------ | -------- | ------------------------------------------------------------ |
| walletAddr | String | 是       | 钱包地址                                                     |
| password   | String | 是       | 支付密码(开启免密支付时可传空串)                             |
| broadcast  | bool   | 是       | 是否发送交易（1为钱包后台发送交易，0为不发送）               |
| walletCall | String | 是       | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |

请求示例
```json
{
	"method": "sdk_cloudWalletTransaction",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "password":"qwer1234",
        "broadcast":1,
        "walletCall":"{\"note\":\"ApplyToBanker\",\"gasLimit\":\"3500000\",\"contractCall\":[{\"contractAddr\":\"bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ\",\"methodName\":\"Transfer\",\"methodParams\":[{\"type\":\"types.Address\",\"value\":\"bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH\"},{\"type\":\"bn.Number-decimal\",\"value\":\"0.0001\"}],\"methodRet\":\"\"}]}"
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
        "tx":"4629F91DD3D6...473BCEF3EE91E750D",
		"hash": "4629F91DD3D6...473BCEF3EE91E750D"
    }
}
```
###  sdk_cloudWalletSignData

数据签名

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| walletAddr | string     | yes        | 钱包地址      |
| password | string | yes | 钱包密码 |
| tbsData | array | yes | 待签名数据列表，item为hexstring (例：["23D464F3BF...C3442247FE5E625A","C9D464F3BF...C3442247FE5E625A"]) |

请求示例
```json
{
    "method": "sdk_cloudWalletSignData",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "password":"qwer1234",
        "tbsData":[
            "23D464F3BF...C3442247FE5E625A",
            "C9D464F3BF...C3442247FE5E625A"
        ]
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
        "signpubKey":"4629F91DD3D6...473BCEF3EE91E750D",
		"signature": 
        [
            "3299791DD3D6...476BBBF3EE91E750C",
            "2099791DD3D6...476BBBF3EE91E750C"
        ]		
	}
}
```

### sdk_getSecretFreePaymentStatus
获取免密授权是否开启

#### 请求格式
请求示例

```json
{
    "method": "sdk_getSecretFreePaymentStatus",
    "params": {}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result": 0  //0为关闭，1为已开启
}
```

### sdk_setSecretFreePayment
开启免密支付授权

#### 请求格式
参数
| name     | type   | required | description                                                  |
| :------- | :----- | :------- | :----------------------------------------------------------- |
| password | string | yes      | 钱包密码                                                     |
| time     | int    | yes      | 请求免密支付的时长，单位是秒(最小：1800， 默认：3600，最大：86400‬) |

请求示例

```json
{
    "method": "sdk_setSecretFreePayment",
    "params": {
        "password":"qwer1234",
        "time":3600
    }
}
```

#### 返回格式
返回示例
```json
{
	"code": 0,
	"msg": "ok",
	"result": {}
}
```

### sdk_cancelSecretFreePayment

取消免密支付授权

#### 请求格式
请求示例

```json
{
    "method": "sdk_cancelSecretFreePayment",
    "params": {}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
}
```

### sdk_getAssetsList
查询默认资产列表

#### 请求格式
请求示例

```json
{
    "method": "sdk_getAssetsList",
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
        {
            "symbol":"BCB",
            "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            "decimals":"9",
            "coinIcon":"http://test.6x.com/coin_icons/bcb.icon",
        },
        {
            "symbol":"USDX",
            "conAddr":"bcbMLpC7HFd8JCm6RXQiu1t7aX4GaiW5c4Cm",
            "decimals":"9",            
            "coinIcon":"http://test.6x.com/coin_icons/usdx.icon"
        }
    ]
}
```

### sdk_getCoinDeatil
查询指定币种余额

#### 请求格式
参数
| name       | type       | required   | description      |
| :--------- | :--------- | :--------- | :--------------- |
| walletAddr | string     | yes        | 钱包地址 |
| conAddr | string     | yes        | 币种合约地址 |
| onChain | bool | yes | 是否直接查询链上余额  （1为链上查询） |

请求示例
```json
{
    "method": "sdk_getCoinDeatil",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "conAddr":"bcbMLpC7HFd8JCm6RXQiu1t7aX4GaiW5c4Cm",
        "onChain":1
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
        "symbol":"USDX",
        "addr":"0x0eF50DD9256D872C6DdB45742dBbD927a697843A",
        "balance":"30.51",
        "conAddr":"0x9F138D5D9e24186eC96B35e5B5530C907860A78d",
        "decimals":"18",
        "coinIcon":"http://test.6x.com/coin_icons/usdx.icon"
    }
}
```

### sdk_getCoinTransactionRecord
查询指定币种交易记录

#### 请求格式
参数
| name       | type   | required | description  |
| :--------- | :----- | :------- | :----------- |
| walletAddr | string | yes      | 钱包地址     |
| conAddr    | string | yes      | 币种合约地址 |
| page       | int    | yes      | 页码从1开始  |
| count      | int    | yes      | 条数         |

请求示例

```json
{
    "method": "sdk_getCoinTransactionRecord",
    "params": {
        "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU",
        "conAddr":"bcbMLpC7HFd8JCm6RXQiu1t7aX4GaiW5c4Cm",
        "page":1,
        "count":10
    }
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
    "msg":"",
	"result": [
        {
            "blockN": 38227106,
            "conAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            "fee": "0.00125",
            "feeName": "BCB",
            "from": "bcbNPVTUmsBFZ1zKYg24vQP26oHeZDy35gYe",
            "memo": "",
            "status": "0x1",
            "timeStamp": "1592374777",
            "to": "bcbCHMRBvnsj6GisZFYG4ApAQaPKkBCUh37B",
            "txHash": "42F48D366D7837FBCCDC9AF963E45FB54E239E912E4F65081E7D14188C48E961",
            "value": "0.101",
            "valueName": "BCB"
        },
        {
            "blockN": 38226125,
            "conAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            "fee": "0.00125",
            "feeName": "BCB",
            "from": "bcbNPVTUmsBFZ1zKYg24vQP26oHeZDy35gYe",
            "memo": "",
            "status": "0x1",
            "timeStamp": "1592372954",
            "to": "bcbCHMRBvnsj6GisZFYG4ApAQaPKkBCUh37B",
            "txHash": "AFF56F4B7DCB117D89E063832F0859CE53055950C125CADFAD7471006C01C4E5",
            "value": "0.174",
            "valueName": "BCB"
        }
    ]
}
```

### sdk_logout
退出登录

#### 请求示例

```json
{
	"method": "sdk_logout",
	"params": {}
}
```

#### 返回格式
返回示例
```json
{
    "code":0,
	"msg": "ok",
	"result":{}
}
```

