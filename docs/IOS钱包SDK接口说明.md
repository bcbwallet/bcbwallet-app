# IOS钱包SDK接口文档说明



## 版本&更新记录

| 版本号  | 作者      | 日期       | 更新内容         |
| ------- | --------- | ---------- | ---------------- |
| v.1.0.0 | bcbwallet | 2019-04-01 | 初始版本         |
| v.1.0.1 | bcbwallet | 2019-07-01 | bcbwallet2.0     |
| v.1.0.2 | bcbwallet | 2019-10-23 | 新增侧链钱包     |
| v.1.0.3 | bcbwallet | 2019-11-25 | 新增域名切换     |
| v.1.0.4 | bcbwallet | 2020-04-21 | 新增托管钱包支持 |

------

------



## 功能说明

本文档提供钱包的SDK访问接口说明。IOS版本。



## 接口访问方式

API调用，返回的内容也是一个json串，里面会携带返回的状态 码以及一些返回的必要参数。



## 1.初始化设置

### 1.注册APP

**说明：初始化接口，建议在APPDelegate的didFinishLaunchingWithOptions中调用**

#### 1.1 方法原型

##### \+(BOOL)registerApp:(NSString \*)appid pushID:(NSString \*)pushid;

 **输入参数说明**

| 参数名 | 类型   | 必须 | 说明                        |
| ------ | ------ | ---- | --------------------------- |
| appid  | string | 是   | 钱包后台分配给第三方的APPID |
| pushid | string | 否   | 接入方自生成的ID（可为空）  |

#### 1.2 返回结果

**示例：返回结果-注册成功**

```java
return YES;
```

**示例：返回结果-注册失败**

```java
return NO;
```



### 2.语言设置

**说明：设置SDK内部接口回调信息的语言类型**

#### 2.1 方法原型

##### +(void)setLanguage:(NSString * )language;

**输入参数说明**

| 参数名   | 类型   | 必须 | 说明                                               |
| -------- | ------ | ---- | -------------------------------------------------- |
| language | string | 是   | SDK中API返回msg语言类型（*cn：中文、en：English*） |



### 3.获取主链及所有侧链ID 

**说明：一般情况是需要在需要切换链之前进行调用获取链的信息，然后选取一个链**

#### 3.1 方法原型

##### -(void)loadAllChainsFinish:(void(^)(ICSDKResultModel * result))finish;

#### 3.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result": ["bcb","yy","jiujiu"]
}
```

**示例：返回结果-错误时**

```java
{
    "code":-1,
	"msg": "error",
    "result":{}
}
```



### 4.链环境设置

**说明：1-3方法拿到所有的链的列表以后选择其中的一个进行切换**

#### 4.1 方法原型

##### \-(BOOL)setWalletChain:(NSString \*)chainId;

**输入参数说明**

| 参数名  | 类型   | 必须 | 说明                             |
| ------- | ------ | ---- | -------------------------------- |
| chainId | string | 是   | 链ID，传空字符串则重置为主链节点 |



### 5.获取域名列表

**说明：一般情况是需要在需要切换域名之前进行调用获取可用域名，然后选取一个重设域名**

#### 5.1 方法原型

##### -(void)getDomainListFinish:(void(^)(ICSDKResultModel * result))finish;

#### 5.2 返回结果

**示例：返回结果-正确时**

```java
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

##### **示例：返回结果-错误时**

```java
{
    "code":-1,
	"msg": "error",
    "result":{}
}
```



### 6.设置域名

**说明：1-5方法拿到所有的域名列表以后选择其中的一个进行设置**

#### 6.1 方法原型

##### -(void)setWalletDomain:(NSString \*)domain finish:(void(^)(ICSDKResultModel * result))finish;

**输入参数说明**

| 参数名 | 类型   | 必须 | 说明               |
| ------ | ------ | ---- | ------------------ |
| domain | string | 是   | 域名地址，不能为空 |

#### 6.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "操作成功",
    "result": {}
}
```

**示例：返回结果-错误时**

```java
{
    "code":-1,
	"msg": "无效域名",
    "result":{}
}
```



## 2.钱包管理

### 1.创建新钱包

#### 1.1 方法原型

##### -(void)createWallet:(NSString \*)name password:(NSString \*)password recommend:(NSString \*)recommend finish:(void(^)(ICSDKResultModel * result))finish;

##### **输入参数说明**

| 参数名    | 类型   | 必须 | 说明             |
| --------- | ------ | ---- | ---------------- |
| name      | string | 是   | 钱包名称         |
| password  | string | 是   | 钱包密码         |
| recommend | string | 否   | 推荐人的钱包地址 |

#### 1.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": 
	{
		"name":"myWallet",
        "mnemonicWords":"eyebrow indoor orbit cinnamon hour gain category spawn walk bind spread clinic",		
		"walletAddr":"bcbPDTi68XwoMgGTwxd7ioZeMHHz7p7ewLtQ"
	}
}
```

**字段说明**

| 字段名        | 类型   | 说明                     |
| ------------- | ------ | ------------------------ |
| name          | string | 钱包名称                 |
| mnemonicWords | string | 钱包的助记词，空格做分割 |
| walletAddr    | string | 钱包地址                 |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "创建钱包失败",
    "result":{}
}
```



### 2.导入私钥生成钱包

#### 2.1 方法原型

##### -(void)importPrivateKey:(NSString \*)name key:(NSString \*)key password:(NSString \*)password recommend:(NSString \*)recommend finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名    | 类型   | 必须 | 说明             |
| --------- | ------ | ---- | ---------------- |
| name      | string | 是   | 钱包名称         |
| key       | string | 是   | 私钥             |
| password  | string | 是   | 钱包密码         |
| recommend | string | 否   | 推荐人的钱包地址 |

#### 2.2 返回结果

**示例：返回结果-正确时**

```java
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

**字段说明**

| 字段名     | 类型   | 说明     |
| ---------- | ------ | -------- |
| name       | string | 钱包名称 |
| walletAddr | string | 钱包地址 |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "导入钱包失败",
    "result":{}
}
```



### 3.导入Keystore生成钱包

#### 3.1 方法原型

##### -(void)importKeystore:(NSString \*)name key:(NSString \*)key password:(NSString \*)password recommend:(NSString \*)recommend finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名    | 类型   | 必须 | 说明             |
| --------- | ------ | ---- | ---------------- |
| name      | string | 是   | 钱包名称         |
| key       | string | 是   | Keystore         |
| password  | string | 是   | 钱包密码         |
| recommend | string | 否   | 推荐人的钱包地址 |

#### 3.2 返回结果

**示例：返回结果-正确时**

```java
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

**字段说明**

| 字段名     | 类型   | 说明     |
| ---------- | ------ | -------- |
| name       | string | 钱包名称 |
| walletAddr | string | 钱包地址 |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "导入钱包失败",
    "result":{}
}
```



### 4.导入助记词生成钱包

#### 4.1 方法原型

##### -(void)importMnemonicWords:(NSString \*)name key:(NSString \*)key password:(NSString \*)password recommend:(NSString \*)recommend finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名    | 类型   | 必须 | 说明             |
| --------- | ------ | ---- | ---------------- |
| name      | string | 是   | 钱包名称         |
| key       | string | 是   | 助记词           |
| password  | string | 是   | 钱包密码         |
| recommend | string | 否   | 推荐人的钱包地址 |

#### 4.2 返回结果

**示例：返回结果-正确时**

```java
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

**字段说明**

| 字段名     | 类型   | 说明     |
| ---------- | ------ | -------- |
| name       | string | 钱包名称 |
| walletAddr | string | 钱包地址 |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "导入钱包失败",
    "result":{}
}
```



### 5.获取所有钱包信息

#### 5.1 方法原型

##### \-(ICSDKResultModel \*)getWallets;

##### 5.2 返回结果

**示例：返回结果-正确时**

```java
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

**字段说明**

| 字段名     | 类型   | 说明     |
| ---------- | ------ | -------- |
| name       | string | 钱包名称 |
| walletAddr | string | 钱包地址 |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "获取钱包失败",
    "result":{}
}
```



### 6.导出助记词

#### 6.1 方法原型

##### -(void)getMnemonicWords:(NSString \*)walletAddr password:(NSString \*)password finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明

| 字段名     | 类型   | 必须 | 说明     |
| ---------- | ------ | ---- | -------- |
| walletAddr | string | 是   | 钱包地址 |
| password   | string | 是   | 钱包密码 |

#### 6.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": 
	{
        "mnemonicWords":"eyebrow indoor orbit cinnamon hour gain category spawn walk bind spread clinic",		
	}
}

```

**字段说明**

| 字段名        | 类型   | 说明         |
| ------------- | ------ | ------------ |
| mnemonicWords | string | 钱包的助记词 |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "获取助记词失败",
    "result":{}
}
```



### 7.导出私钥

#### 7.1 方法原型

##### -(void)exportPrivateKey:(NSString \*)walletAddr password:(NSString \*)password finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明     |
| ---------- | ------ | ---- | -------- |
| walletAddr | string | 是   | 钱包地址 |
| password   | string | 是   | 钱包密码 |

#### 7.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": 
	{				 "privateKey":"0x98BB2E49822A48728E3CBCFD1A933C1FC500A6204453E7DB85F84EFB90146600"
	}
}

```

**字段说明**

| 字段名     | 类型   | 说明     |
| ---------- | ------ | -------- |
| privateKey | string | 明文私钥 |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "导出私钥失败",
    "result":{}
}
```



### 8.导出Keystore

#### 8.1 方法原型

##### -(void)exportKeystore:(NSString \*)walletAddr password:(NSString \*)password finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明     |
| ---------- | ------ | ---- | -------- |
| walletAddr | string | 是   | 钱包地址 |
| password   | string | 是   | 钱包密码 |

#### 8.2 返回结果

**示例：返回结果-正确时**

```java
{
	"code": 0,
	"msg": "ok",
	"result": {
		"keystore": "{\"address\":\"bcbMd6xUDQLoivMT45Qp8o7M8vjN5wRyHAF3\",\"crypto\":{\"cipher\":\"aes-128-ctr\",\"cipherparams\":{\"iv\":\"026fad88d89baadb9110ae533ef8039d\"},\"ciphertext\":\"7c1dafc7e541cc14d0fe11773fc4d2da6933384d5279984df57693f98d3be4a8\",\"kdf\":\"scrypt\",\"kdfparams\":{\"dklen\":32,\"n\":262144,\"p\":1,\"r\":8,\"salt\":\"c1fe07bed958a78763ac5816c7dbad9351accd80c18bbc70aa3279d5fb34638f\"},\"mac\":\"d6042cf16b55c3bac25f392d1d33476e84e5276b672ad8e77ccd1713d586e18d\"},\"id\":\"eabffab4-5c21-46a4-a709-9699a72d1339\",\"version\":3}"
	}
}

```

**字段说明**

| 字段名   | 类型   | 说明         |
| -------- | ------ | ------------ |
| keystore | string | 明文keystore |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "导出keystore失败",
    "result":{}
}
```



### 9.验证钱包密码

#### 9.1 方法原型

##### -(void)verifyPassword:(NSString \*)walletAddr password:(NSString \*)password finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明     |
| ---------- | ------ | ---- | -------- |
| walletAddr | string | 是   | 钱包地址 |
| password   | string | 是   | 钱包密码 |

#### 9.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": {}
}

```

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "密码错误",
    "result":{}
}
```



### 10.修改钱包密码（主链钱包对应的所有侧链钱包密码唯一）

#### 10.1 方法原型

##### -(void)changePassword:(NSString \*)walletAddr oldPassword:(NSString \*)oldPassword newPassword:(NSString \*)newPassword finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名      | 类型   | 必须 | 说明       |
| ----------- | ------ | ---- | ---------- |
| walletAddr  | string | 是   | 钱包地址   |
| oldPassword | string | 是   | 原钱包密码 |
| newPassword | string | 是   | 新钱包密码 |

#### 10.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": {}
}
```

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "原密码输入错误",
    "result":{}
}
```



### 11.修改钱包名称（主链钱包对应的所有侧链钱包名称唯一）

#### 11.1 方法原型

##### -(void)changeWalletName:(NSString \*)walletAddr newName:(NSString \*)newName finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明       |
| ---------- | ------ | ---- | ---------- |
| walletAddr | string | 是   | 钱包地址   |
| newName    | string | 是   | 新钱包名称 |

#### 11.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result": {
        "name":"newWallet",
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5",
    }
}

```

**字段说明**

| 字段名     | 类型   | 说明     |
| ---------- | ------ | -------- |
| name       | string | 钱包名称 |
| walletAddr | string | 钱包地址 |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "钱包名称格式错误",
    "result":{}
}
```



### 12.删除钱包（主链钱包对应的其他侧链钱包同步删除）

#### 12.1 方法原型

##### -(void)deleteWallet:(NSString \*)walletAddr password:(NSString \*)password finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明     |
| ---------- | ------ | ---- | -------- |
| walletAddr | string | 是   | 钱包地址 |
| password   | string | 是   | 钱包密码 |

#### 12.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": {}
}

```

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "密码错误",
    "result":{}
}
```



## 3.支付及交易查询

### 1.钱包转账

#### 1.1 方法原型

##### -(void)walletTransation:(NSString \*)walletAddr password:(NSString \*)password coinAddr:(NSString \*)coinAddr toAddr:(NSString \*)toAddr value:(NSString \*)value note:(NSString \*)note  finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                              |
| ---------- | ------ | ---- | ------------------------------------------------- |
| walletAddr | string | 是   | 钱包地址                                          |
| password   | string | 是   | 钱包密码                                          |
| coinAddr   | string | 是   | 要转账币种的合约地址                              |
| toAddr     | string | 是   | 转账到的目标地址                                  |
| value      | string | 是   | 转账的金额，例如"102.23"                          |
| note       | string | 否   | 转账的备注，对于BCB链，这个字段最终会写入到区块中 |

#### 1.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": 
	{	
		"txHash":"0x0F8642968E48A16316CD499BF142E15EEFF03BE44816796AF87DDC2F1B72BBA4",
	}
}
```

**字段说明**

| 字段名 | 类型   | 说明             |
| ------ | ------ | ---------------- |
| txHash | string | 转账的链上hash值 |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "转账失败",
    "result":{}
}
```



### 2.通用支付-通用型合约支付接口

#### 2.1 方法原型

##### -(void)walletCommonPay:(NSString \*)walletAddr version:(int)version password:(NSString \*)password walletCall:(NSString \*)walletCall finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| walletAddr | string | 是   | 钱包地址                                                     |
| version    | Int    | 是   | 1.0的支付传1， 2.0的支付传2，  3.0的支付传                   |
| password   | string | 是   | 钱包密码                                                     |
| walletCall | string | 是   | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |

**示例：1.0支付walletCall**

walletCall字符串格式

```java
"{\"conAddr\":\"bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9\",\"methodName\":\"BuyXid\",\"methodParam\":[{\"name\":\"_affCode\",\"type\":\"int64\",\"value\":\"12345678\"},{\"name\":\"_team\",\"type\":\"int64\",\"value\":\"0\"},{\"name\":\"_bcb\",\"type\":\"Number-decimal\",\"value\":\"2.5\"}],\"methodRet\":\"smc.Error\"}"
```

展开后格式

```java
{
    "conAddr":"bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9",
    "methodName":"BuyXid",
    "methodParam":
    [
        {
            "name":"_affCode",
            "type":"int64",
            "value":"12345678"
        },
        {
            "name":"_team",
            "type":"int64",
            "value":"0"
        },
        {
            "name":"_bcb",
            "type":"Number-decimal",
            "value":"2.5"
        }
    ],
    "methodRet":"smc.Error"
}
```

**示例：2.0支付walletCall**

walletCall字符串格式

```java
"{\"note\":\"ApplyToBanker\",\"gasLimit\":\"3500000\",\"contractCall\":[{\"contractAddr\":\"bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ\",\"methodName\":\"Transfer\",\"methodParams\":[{\"type\":\"types.Address\",\"value\":\"bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH\"},{\"type\":\"bn.Number-decimal\",\"value\":\"0.1\"}],\"methodRet\":\"\"}]}"
```

展开后格式

```java
{
	"note": "ApplyToBanker",
	"gasLimit": "3500000",
	"contractCall": [{
		"contractAddr": "bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ",
		"methodName": "Transfer",
		"methodParams": [{
			"type": "types.Address",
			"value": "bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH"
		}, {
			"type": "bn.Number-decimal",
			"value": "0.1"
		}],
		"methodRet": ""
	}]
}
```

**示例：3.0支付walletCall**

walletCall字符串格式

```java
"{\"note\":\"request-banker\",\"gasLimit\":\"3500000\",\"calls\":[{\"contract\":\"bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ\",\"method\":\"Transfer(types.Address,bn.Number)\",\"params\":[\"bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH\",\"10\"]}]}"
```

展开后格式

```java
{
	"note": "request-banker",
	"gasLimit": "3500000",
	"calls": [{
		"contract": "bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ",
		"method": "Transfer(types.Address,bn.Number)",
		"params": ["bcbJkX5Hcfdewinsc2DkGA5LPNRQix93iwDH", "10"]
	}]
}
```

#### 2.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": 
	{	
        "txHash":"0x0F8642968E48A16316CD499BF142E15EEFF03BE44816796AF87DDC2F1B72BBA4"
	}
}
```

**字段说明**

| 字段名 | 类型   | 说明             |
| ------ | ------ | ---------------- |
| txHash | string | 转账的链上hash值 |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "支付失败",
    "result":{}
}
```



### 3.查询指定地址资产

#### 3.1 方法原型

##### -(void)getAddrsBalance:(NSString \*)walletAddr legalSymbol:(NSString \*)legalSymbol finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名      | 类型   | 必须 | 说明                                           |
| ----------- | ------ | ---- | ---------------------------------------------- |
| walletAddr  | string | 是   | 钱包地址                                       |
| legalSymbol | string | 是   | 资产的法币计价单位，人民币为：CNY；美元为：USD |

#### 3.2 返回结果

**返回结果-正确时**

```java
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
            "conAddr":"bcbtest6e8CEdrcGzX79kRCGJG6h5jVdpdkGDniU",
            "name":"Diamond Coin",
            "symbol":"DC",
            "balance":"0",
            "last":"2019-04-01T14:21:00.8344546+08:00",
            "decimals":"9",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/DC.png",
            "legalValue":"0",
            "isToken":true,
            "idx":2,
            "feeInfo":null
        },
        {
            "addr":"bcbtestCTLvcA7pa1RqCncL2fRcALgRrVYudJNeE",
            "coinType":"0x1001",
            "conAddr":"bcbtestHStZsJDbP945H1GbZSJx3xDegtMehMNWK",
            "name":"USDX",
            "symbol":"USDX",
            "balance":"0",
            "last":"2019-04-01T14:21:00.8344578+08:00",
            "decimals":"9",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/USDX.png",
            "legalValue":"0",
            "isToken":true,
            "idx":4,
            "feeInfo":null
        }
    ]
}

```

**字段说明**

| 字段名     | 类型   | 说明                                        |
| ---------- | ------ | ------------------------------------------- |
| addr       | string | 钱包地址                                    |
| coinType   | string | 币种主链编号，第三方应用无需关心            |
| conAddr    | string | 币种合约地址                                |
| name       | string | 币种名称                                    |
| symbol     | string | 币种代号                                    |
| balance    | string | 地址的此币种余额                            |
| last       | string | 最后一次更新时间                            |
| decimals   | string | 币种精度                                    |
| coinIcon   | string | 币种图标                                    |
| legalValue | string | 币种的法币价值                              |
| isToken    | bool   | 是否为代币，true表示代币；false表示主链本币 |
| idx        | int    | 币种在钱包后台的排序，，第三方应用无需关心  |
| feeInfo    | object | 币种的转账手续费描述信息                    |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "获取指定地址资产表失败",
    "result":{}
}
```



### 4.获取系统可添加资产列表

#### 4.1 方法原型

##### -(void)getAssets:(NSString \*)walletAddr finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明     |
| ---------- | ------ | ---- | -------- |
| walletAddr | string | 是   | 钱包地址 |

#### 4.2 返回结果

**返回结果-正确时**

```java
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
            "id":2,
            "cid":22,
            "coinType":"0x1001",
            "chainType":1,
            "chainName":"BCB链",
            "name":"Diamond Coin",
            "name_customer":"Diamond Coin",
            "symbol":"DC",
            "symbol_customer":"DC",
            "decimals":"9",
            "conAddr":"bcbtest6e8CEdrcGzX79kRCGJG6h5jVdpdkGDniU",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/DC.png",
            "config":1,
            "idx":2,
            "appid":"1",
            "modifyTime":"2018-09-27T21:58:30"
        },
        {
            "id":6,
            "cid":21,
            "coinType":"0x1001",
            "chainType":1,
            "chainName":"BCB链",
            "name":"USDX",
            "name_customer":"USDX",
            "symbol":"USDX",
            "symbol_customer":"USDX",
            "decimals":"9",
            "conAddr":"bcbtestHStZsJDbP945H1GbZSJx3xDegtMehMNWK",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/USDX.png",
            "config":1,
            "idx":4,
            "appid":"1",
            "modifyTime":"2018-10-30T17:26:02"
        }
    ]
}

```

**字段说明**

| 字段名          | 类型   | 说明                                     |
| --------------- | ------ | ---------------------------------------- |
| id              | int    | 序号                                     |
| cid             | int    | 后台字段，第三方应用无需关心             |
| coinType        | string | 币种主链编号，第三方应用无需关心         |
| chainType       | int    | 第三方应用无需关心                       |
| chainName       | string | 链的名称说明，第三方应用无需关心         |
| name            | string | 币种名称                                 |
| name_customer   | string | 客户自定义的币种名称，第三方应用无需关心 |
| symbol          | string | 币种符号                                 |
| symbol_customer | string | 客户自定义的币种符号，第三方应用无需关心 |
| decimals        | string | 币种小数点精度                           |
| conAddr         | string | 币种合约地址                             |
| coinIcon        | string | 币种logo的地址                           |
| config          | int    | 币种是否可以配置，第三方应用无需关心     |
| idx             | int    | 币种的自定义排序，第三方应用无需关心     |
| appid           | int    | 应用id，第三方应用无需关心               |
| modifyTime      | string | 最后一次更新时间                         |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "查询失败",
    "result":{}
}
```



### 5.查询指定地址、指定币种信息

#### 5.1 方法原型

##### -(void)getCoinDeatil:(NSString \*)walletAddr coinAddr:(NSString \*)coinAddr legalSymbol:(NSString \*)legalSymbol finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名      | 类型   | 必须 | 说明                                               |
| ----------- | ------ | ---- | -------------------------------------------------- |
| walletAddr  | string | 是   | 钱包地址                                           |
| conAddr     | string | 是   | 币种合约地址                                       |
| legalSymbol | string | 是   | 币种资产的法币计价单位，人民币为：CNY；美元为：USD |

#### 5.2 返回结果

**返回结果-正确时**

```java
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

**字段说明**

| 字段名     | 类型   | 说明                             |
| ---------- | ------ | -------------------------------- |
| addr       | string | 地址                             |
| coinType   | string | 币种主链编号，第三方应用无需关心 |
| conAddr    | string | 币种合约地址                     |
| name       | string | 币种名称                         |
| symbol     | string | 币种符号                         |
| balance    | string | 地址的此币种余额                 |
| last       | string | 最后一次更新时间                 |
| decimals   | string | 币种小数点精度                   |
| coinIcon   | string | 币种logo的地址                   |
| legalValue | string | 币种的法币价值                   |
| isToken    | bool   | 是否为代币                       |
| idx        | int    | 第三方应用无需关心               |
| feeInfo    | object | 币种手续费描述信息               |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "查询失败",
    "result":{}
}
```



### 6.查询指定币种交易记录

#### 6.1 方法原型

##### -(void)getCoinTransactionDetail:(NSString \*)walletAddr conAddr:(NSString \*)coinAddr page:(NSInteger)page count:(NSInteger)count finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明         |
| ---------- | ------ | ---- | ------------ |
| walletAddr | string | 是   | 钱包地址     |
| conAddr    | string | 是   | 币种合约地址 |
| page       | int    | 是   | 页码从0开始  |
| count      | int    | 是   | 条数         |

#### 6.2 返回结果

**返回结果-正确时**

```java
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

**字段说明**

| 字段名          | 类型   | 说明                             |
| --------------- | ------ | -------------------------------- |
| id              | int    | 第三方应用无需关心               |
| coinType        | string | 币种主链编号，第三方应用无需关心 |
| from            | string | 转出方地址                       |
| to              | string | 收款人地址                       |
| conAddr         | string | 币种合约地址                     |
| value           | string | 转账金额                         |
| valueName       | string | 转账金额名称                     |
| fee             | string | 手续费金额份额                   |
| feeName         | string | 手续费币种名称                   |
| timeStamp       | string | 转账时间戳                       |
| blockN          | string | 区块号                           |
| source          |        | 第三方无需关心                   |
| txHash          | string | 交易hash                         |
| memo            | string | 交易备注信息                     |
| status          | string | 交易是否成功，"0x1"表示成功      |
| balanceFromFlag | int    | 第三方无需关心                   |
| balanceToFlag   | int    | 第三方无需关心                   |
| pushFromCnt     | int    | 第三方无需关心                   |
| modifyTime      | string | 最后一次修改时间                 |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "查询失败",
    "result":{}
}
```



## 4.托管云钱包管理

### 1.设置域名

**说明：初始化设置**

#### 1.1 方法原型

##### -(BOOL)setCloudDomain:(NSString \*)domain;

**参数字段说明**

| 字段名 | 类型   | 必须 | 说明                                                         |
| ------ | ------ | ---- | ------------------------------------------------------------ |
| domain | String | 是   | 域名（例："https://tcapi.iwallet.cloud/pkey_api"--云钱包测试后台） |

#### 1.2 返回结果

**示例：返回结果-设置成功**

```java
return YES;
```

**示例：返回结果-设置失败**

```java
return NO;
```



### 2.设置商户信息

**说明：初始化设置**

#### 2.1 方法原型

##### -(BOOL)setMerchantId:(NSString \*)mechantId remoteDHPubKey:(NSString \*)remoteDHPubKey;

**参数字段说明**

| 字段名         | 类型   | 必须 | 说明         |
| -------------- | ------ | ---- | ------------ |
| mechantId      | String | 是   | 商户ID       |
| remoteDHPubKey | String | 是   | 商户对应公钥 |

#### 2.2 返回结果

**示例：返回结果-设置成功**

```java
return YES;
```

**示例：返回结果-设置失败**

```java
return NO;
```



### 3.获取已绑定账户

#### 3.1 方法原型

##### -(NSString \*)hasBoundAccount;

#### 3.2 返回结果

**示例：返回结果-空字符串即表示未绑定过账户**

```java
return @"+86139***";
```



### 4.获取验证码

#### 4.1 方法原型

##### -(void)getCode:(NSString \*)account finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名  | 类型   | 必须 | 说明                                                         |
| ------- | ------ | ---- | ------------------------------------------------------------ |
| account | string | 是   | 手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |

#### 4.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
	"result": {}
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "发送失败",
    "result":{}
}
```



### 5.绑定账号

#### 5.1 方法原型

##### -(void)bindAccount:(NSString \*)account code:(NSString \*)code password:(NSString \*)password finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名   | 类型   | 必须 | 说明                                                         |
| -------- | ------ | ---- | ------------------------------------------------------------ |
| account  | String | 是   | 手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |
| code     | String | 是   | 验证码                                                       |
| password | String | 是   | 账号密码(可传空串)                                           |

#### 5.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
	"result": {}
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "发送失败",
    "result":{}
}
```



### 6.绑定新的验证方式

#### 6.1 方法原型

##### -(void)addVerify:(NSString \*)account code:(NSString \*)code  finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名  | 类型   | 必须 | 说明                                                         |
| ------- | ------ | ---- | ------------------------------------------------------------ |
| account | String | 是   | 手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |
| code    | String | 是   | 验证码                                                       |

#### 6.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
	"result": {}
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1,
	"msg": "该账户已存在",
    "result":{}
}
```



### 7.创建云钱包

#### 7.1 方法原型

##### -(void)createCloudWallet:(NSString \*)chainType finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名    | 类型   | 必须 | 说明                         |
| --------- | ------ | ---- | ---------------------------- |
| chainType | String | 是   | 主链，例如BCB/ETH/BTC/EOS... |

#### 7.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
	"result": {
		"address": "bcbH8EnQ12jEeTXzPWKByVidjmaGXSTbHn3T"
	}
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
    "result":{}
}
```



### 8.获取云钱包地址列表

#### 8.1 方法原型

##### -(void)getCloudWalletList:(NSString \*)chainType finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名    | 类型   | 必须 | 说明                         |
| --------- | ------ | ---- | ---------------------------- |
| chainType | String | 是   | 主链，例如BCB/ETH/BTC/EOS... |

#### 8.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
	"result": [
		"bcbH8EnQ12jEeTXzPWKByVidjmaGXSTbHn3T",
        "bcbFdDBN2k3Xs6dp4FfwLCy9cMPGjNusGNxT"
	]
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
    "result":{}
}
```



### 9.云钱包通用支付

#### 9.1 方法原型

##### -(void)cloudWalletTransation:(NSString \*)walletAddr password:(NSString \*)password chainType:(NSString \*)chainType walletCall:(NSString \*)walletCall finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| walletAddr | String | 是   | 钱包地址                                                     |
| password   | String | 是   | 账号密码(可传空串)                                           |
| chainType  | String | 是   | 主链，例如BCB/ETH/BTC/EOS...                                 |
| walletCall | String | 是   | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |

#### 9.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
    "result": {
        "txHash": "0x0F8642968E48A16316CD499BF142E15EEFF03BE44816796AF87DDC2F1B72BBA4"
    }
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
    "result":{}
}
```



### 10.云钱包交易签名

#### 10.1 方法原型

##### -(void)signTransation:(NSString \*)walletAddr password:(NSString \*)password chainType:(NSString \*)chainType walletCall:(NSString \*)walletCall finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| walletAddr | String | 是   | 钱包地址                                                     |
| password   | String | 是   | 账号密码(可传空串)                                           |
| chainType  | String | 是   | 主链，例如BCB/ETH/BTC/EOS...                                 |
| walletCall | String | 是   | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |

#### 10.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
    "result": {
        "txData": "<bcb>…."
    }
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
    "result":{}
}
```



### 11.查询指定地址资产

#### 11.1 方法原型

##### -(void)getCloudAddrsBalance:(NSString \*)walletAddr legalSymbol:(NSString \*)legalSymbol finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名      | 类型   | 必须 | 说明                                           |
| ----------- | ------ | ---- | ---------------------------------------------- |
| walletAddr  | string | 是   | 钱包地址                                       |
| legalSymbol | string | 是   | 资产的法币计价单位，人民币为：CNY；美元为：USD |

#### 11.2 返回结果

**返回结果-正确时**

```java
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
            "conAddr":"bcbtest6e8CEdrcGzX79kRCGJG6h5jVdpdkGDniU",
            "name":"Diamond Coin",
            "symbol":"DC",
            "balance":"0",
            "last":"2019-04-01T14:21:00.8344546+08:00",
            "decimals":"9",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/DC.png",
            "legalValue":"0",
            "isToken":true,
            "idx":2,
            "feeInfo":null
        },
        {
            "addr":"bcbtestCTLvcA7pa1RqCncL2fRcALgRrVYudJNeE",
            "coinType":"0x1001",
            "conAddr":"bcbtestHStZsJDbP945H1GbZSJx3xDegtMehMNWK",
            "name":"USDX",
            "symbol":"USDX",
            "balance":"0",
            "last":"2019-04-01T14:21:00.8344578+08:00",
            "decimals":"9",
            "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/USDX.png",
            "legalValue":"0",
            "isToken":true,
            "idx":4,
            "feeInfo":null
        }
    ]
}

```

**字段说明**

| 字段名     | 类型   | 说明                                        |
| ---------- | ------ | ------------------------------------------- |
| addr       | string | 钱包地址                                    |
| coinType   | string | 币种主链编号，第三方应用无需关心            |
| conAddr    | string | 币种合约地址                                |
| name       | string | 币种名称                                    |
| symbol     | string | 币种代号                                    |
| balance    | string | 地址的此币种余额                            |
| last       | string | 最后一次更新时间                            |
| decimals   | string | 币种精度                                    |
| coinIcon   | string | 币种图标                                    |
| legalValue | string | 币种的法币价值                              |
| isToken    | bool   | 是否为代币，true表示代币；false表示主链本币 |
| idx        | int    | 币种在钱包后台的排序，，第三方应用无需关心  |
| feeInfo    | object | 币种的转账手续费描述信息                    |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "获取指定地址资产表失败",
    "result":{}
}
```



### 12.查询指定地址、指定币种信息

#### 12.1 方法原型

##### -(void)getCloudCoinDeatil:(NSString \*)walletAddr coinAddr:(NSString \*)coinAddr legalSymbol:(NSString \*)legalSymbol finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名      | 类型   | 必须 | 说明                                               |
| ----------- | ------ | ---- | -------------------------------------------------- |
| walletAddr  | string | 是   | 钱包地址                                           |
| conAddr     | string | 是   | 币种合约地址                                       |
| legalSymbol | string | 是   | 币种资产的法币计价单位，人民币为：CNY；美元为：USD |

#### 12.2 返回结果

**返回结果-正确时**

```java
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

**字段说明**

| 字段名     | 类型   | 说明                             |
| ---------- | ------ | -------------------------------- |
| addr       | string | 地址                             |
| coinType   | string | 币种主链编号，第三方应用无需关心 |
| conAddr    | string | 币种合约地址                     |
| name       | string | 币种名称                         |
| symbol     | string | 币种符号                         |
| balance    | string | 地址的此币种余额                 |
| last       | string | 最后一次更新时间                 |
| decimals   | string | 币种小数点精度                   |
| coinIcon   | string | 币种logo的地址                   |
| legalValue | string | 币种的法币价值                   |
| isToken    | bool   | 是否为代币                       |
| idx        | int    | 第三方应用无需关心               |
| feeInfo    | object | 币种手续费描述信息               |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "查询失败",
    "result":{}
}
```



### 13.查询指定地址、指定币种交易记录

#### 13.1 方法原型

##### -(void)getCloudCoinTransactionDetail:(NSString \*)walletAddr conAddr:(NSString \*)coinAddr page:(NSInteger)page count:(NSInteger)count finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明         |
| ---------- | ------ | ---- | ------------ |
| walletAddr | string | 是   | 钱包地址     |
| conAddr    | string | 是   | 币种合约地址 |
| page       | int    | 是   | 页码从0开始  |
| count      | int    | 是   | 条数         |

#### 13.2 返回结果

**返回结果-正确时**

```java
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

**字段说明**

| 字段名          | 类型   | 说明                             |
| --------------- | ------ | -------------------------------- |
| id              | int    | 第三方应用无需关心               |
| coinType        | string | 币种主链编号，第三方应用无需关心 |
| from            | string | 转出方地址                       |
| to              | string | 收款人地址                       |
| conAddr         | string | 币种合约地址                     |
| value           | string | 转账金额                         |
| valueName       | string | 转账金额名称                     |
| fee             | string | 手续费金额份额                   |
| feeName         | string | 手续费币种名称                   |
| timeStamp       | string | 转账时间戳                       |
| blockN          | string | 区块号                           |
| source          |        | 第三方无需关心                   |
| txHash          | string | 交易hash                         |
| memo            | string | 交易备注信息                     |
| status          | string | 交易是否成功，"0x1"表示成功      |
| balanceFromFlag | int    | 第三方无需关心                   |
| balanceToFlag   | int    | 第三方无需关心                   |
| pushFromCnt     | int    | 第三方无需关心                   |
| modifyTime      | string | 最后一次修改时间                 |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "查询失败",
    "result":{}
}
```

### 14.数据签名

#### 14.1 方法原型

##### -(void)secretSign:(NSString \*)content finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名  | 类型   | 必须 | 说明                    |
| ------- | ------ | ---- | ----------------------- |
| content | string | 是   | 待签名数据（hexstring） |

#### 14.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": {
		"pubKey": "4C24B251B0A1FEDCE66DDD37A3CBC4FC46B5173A201BBC840A98FB5F29C496F3",
		"signature": "E8C0B40BE53F9869D8E51B830936C131112083DC746CCE16AA3BF002D24A8B16A0CEDA79EF803B39CF8D7539E0C685DEA47CBE2524B7F8D36590816928559908"
	}
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "fail",
    "result":""
}
```



### 15.数据验签

#### 15.1 方法原型

##### -(void)verifySign:(NSString \*)content signature:(NSString \*)signature finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名    | 类型   | 必须 | 说明                    |
| --------- | ------ | ---- | ----------------------- |
| content   | string | 是   | 待验签内容（hexstring） |
| signature | string | 是   | 签名（hexstring）       |

#### 15.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "success",
	"result": ""
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "verify fail",
    "result":""
}
```



## 5.OTC及闪兑模块

### 1.OTC模块皮肤主题设置

**说明：进入OTC模块前设置**

#### 1.1 方法原型

##### -(void)setOtcTheme:(ICOTCThemeType)theme;

**参数字段说明**

| 字段名 | 类型 | 必须 | 说明                     |
| ------ | ---- | ---- | ------------------------ |
| theme  | int  | 是   | 0：白色主题、1：暗色主题 |



### 2.OTC买币强制绑定银行卡设置

**说明：进入OTC模块前设置**

#### 2.1 方法原型

##### -(void)setOtcBuyBindBankCard:(BOOL)bind;

**参数字段说明**

| 字段名 | 类型 | 必须 | 说明                      |
| ------ | ---- | ---- | ------------------------- |
| bind   | Bool | 是   | 默认不强制，强制绑定为YES |



### 3.OTC入口

#### 3.1 方法原型

##### [[OTCStart manager] OTCStart];



### 4.闪兑入口

#### 4.1 方法原型

##### [[OTCStart manager] fastexStart];



### 5.退出OTC/闪兑

说明：通过ICWalletSDKDelegate退出模块



## 6.工具

### 1.加密

#### 1.1 方法原型

##### -(void)encryptContent:(NSString \*)content finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名  | 类型   | 必须 | 说明     |
| ------- | ------ | ---- | -------- |
| content | string | 是   | 加密内容 |

#### 1.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": "/suzXLeVk3tU3AmFe1/lhA=="
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "fail",
    "result":""
}
```



### 2.解密

#### 2.1 方法原型

##### -(void)decryptContent:(NSString \*)content finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名  | 类型   | 必须 | 说明     |
| ------- | ------ | ---- | -------- |
| content | string | 是   | 解密内容 |

#### 2.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": "123"
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "fail",
    "result":""
}
```



### 3.生成密钥对

#### 3.1 方法原型

##### -(void)genKeyPairFinish:(void(^)(ICSDKResultModel * result))finish;

#### 3.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": {
		"mnemonic": "step easy argue casual one hour engage excite speak slab detail blossom",
		"priKey": "29DA5671048493912669E3F309DFE8D1703CD2DB11AC15B973E6035A4D153D1F",
		"pubKey": "46BD93A849ACA46F3B51728C36DE40BC27A15B3760B89243DEE624B92A1BB681"
	}
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "fail",
    "result":""
}
```



### 4.私钥签名

#### 4.1 方法原型

##### -(void)genericSign:(NSString \*)priKey data:(NSString \*)data finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名 | 类型   | 必须 | 说明          |
| ------ | ------ | ---- | ------------- |
| priKey | string | 是   | 私钥hex       |
| data   | string | 是   | 待签名内容hex |

#### 4.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result": {
		"pubKey": "4C24B251B0A1FEDCE66DDD37A3CBC4FC46B5173A201BBC840A98FB5F29C496F3",
		"signature": "E8C0B40BE53F9869D8E51B830936C131112083DC746CCE16AA3BF002D24A8B16A0CEDA79EF803B39CF8D7539E0C685DEA47CBE2524B7F8D36590816928559908"
	}
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "fail",
    "result":""
}
```



### 5.数据验签

#### 5.1 方法原型

##### -(void)verifySign:(NSString \*)type data:(NSString \*)data pubKey:(NSString \*)pubKey signature:(NSString \*)signature finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名    | 类型   | 必须 | 说明                    |
| --------- | ------ | ---- | ----------------------- |
| type      | string | 是   | 算法，目前只支持ed25519 |
| data      | string | 是   | 待验签内容（hexstring） |
| pubKey    | string | 是   | 验签公钥（hexstring）   |
| signature | string | 是   | 签名（hexstring）       |

#### 5.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "success",
	"result": ""
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "verify fail",
    "result":""
}
```



### 6.根据助记词返回对应钱包地址

#### 6.1 方法原型

##### -(void)getAddrFromMnemonicWords:(NSString \*)mnemonicWords finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名        | 类型   | 必须 | 说明   |
| ------------- | ------ | ---- | ------ |
| mnemonicWords | string | 是   | 助记词 |

#### 6.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
    "result": {
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
    }
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "fail",
    "result":""
}
```



### 7.根据私钥返回对应钱包地址

#### 7.1 方法原型

##### -(void)getAddrFromPrivateKey:(NSString \*)privateKey finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明 |
| ---------- | ------ | ---- | ---- |
| privateKey | string | 是   | 私钥 |

#### 7.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
    "result": {
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
    }
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "fail",
    "result":""
}
```



### 8.根据Keystore返回对应钱包地址

#### 8.1 方法原型

##### -(void)getAddrFromKeystore:(NSString \*)keystore password:(NSString \*)password finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名   | 类型   | 必须 | 说明     |
| -------- | ------ | ---- | -------- |
| keystore | string | 是   | keystore |
| password | string | 是   | 密码     |

#### 8.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
    "result": {
        "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"
    }
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "fail",
    "result":""
}
```

