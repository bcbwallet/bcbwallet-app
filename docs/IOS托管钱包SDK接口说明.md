## IOS托管钱包SDK接口文档说明



### 版本&更新记录

| 版本号  | 作者        | 日期       | 更新内容 |
| ------- | ----------- | ---------- | -------- |
| v.1.0.0 | cloudwallet | 2020-06-16 | 初始版本 |

------

------



### 功能说明

本文档提供托管钱包的SDK访问接口说明。IOS版本。



### 接口访问方式

API调用，返回的内容也是一个json串，里面会携带返回的状态 码以及一些返回的必要参数。



### 1.初始化设置

#### 1.商户信息设置

**说明：初始化接口，建议在APPDelegate的didFinishLaunchingWithOptions中调用**

##### 1.1 方法原型

\-(BOOL)registerApp:(NSString \*)appId apiKey:(NSString \*)apiKey domain:(NSString \*)domain;

 **输入参数说明**

| 参数名 | 类型   | 必须 | 说明                                                         |
| ------ | ------ | ---- | ------------------------------------------------------------ |
| appId  | string | 是   | 云钱包后台分配的App唯一ID                                    |
| apiKey | string | 是   | 托管分配的密钥                                               |
| domain | string | 是   | 云钱包后台域名域名（例："https://api.iwallet.cloud/pkey_api"--云钱包后台） |

##### 1.2 返回结果

**示例：返回结果-注册成功**

```java
return YES;
```

**示例：返回结果-注册失败**

```java
return NO;
```



#### 2.设置链

##### 1.1 方法原型

\-(BOOL)setChainType:(NSString \*)chainType;

 **输入参数说明**

| 参数名    | 类型   | 必须 | 说明                                   |
| --------- | ------ | ---- | -------------------------------------- |
| chainType | string | 是   | 链类型（例：BCB、BCBJF、BCBTJF......） |

##### 1.2 返回结果

**示例：返回结果-设置成功**

```java
return YES;
```

**示例：返回结果-设置失败**

```java
return NO;
```



### 2.钱包地址相关信息查询

#### 1.查询默认资产列表

##### 1.1 方法原型

 -(void)getAssetsListFinish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

无

##### 1.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result":[
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

**字段说明**

| 字段名   | 类型   | 说明     |
| -------- | ------ | -------- |
| symbol   | string | 符号     |
| conAddr  | string | 合约地址 |
| decimals | string | 精度     |
| coinIcon | string | 币种图标 |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "获取资产列表失败",
    "result":{}
}
```



#### 2.查询指定币种余额

##### 2.1 方法原型

 -(void)getCoinDeatil:(NSString \*)walletAddr coinAddr:(NSString \*)coinAddr onChain:(BOOL)onChain finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                     |
| ---------- | ------ | ---- | ---------------------------------------- |
| walletAddr | string | 是   | 钱包地址                                 |
| conAddr    | string | 是   | 币种合约地址                             |
| onChain    | bool   | 是   | 是否直接查询链上余额  （true为链上查询） |

##### 2.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result":{
        "symbol":"USDX",
        "addr":"0x0eF50DD9256D872C6DdB45742dBbD927a697843A",
        "balance":"30.51",
        "conAddr":"0x9F138D5D9e24186eC96B35e5B5530C907860A78d",
        "decimals":"18",
        "coinIcon":"http://test.6x.com/coin_icons/usdx.icon"
    }
}
```

**字段说明**

| 字段名   | 类型   | 说明     |
| -------- | ------ | -------- |
| symbol   | string | 符号     |
| addr     | string | 地址     |
| balance  | string | 余额     |
| conAddr  | string | 合约地址 |
| decimals | string | 精度     |
| coinIcon | string | 币种图标 |

**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "查询失败",
    "result":{}
}
```



#### 3.查询指定币种交易记录

##### 3.1 方法原型

 -(void)getCoinTransactionRecord:(NSString \*)walletAddr conAddr:(NSString \*)coinAddr page:(NSInteger)page count:(NSInteger)count finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明         |
| ---------- | ------ | ---- | ------------ |
| walletAddr | string | 是   | 钱包地址     |
| conAddr    | string | 是   | 币种合约地址 |
| page       | int    | 是   | 页码从1开始  |
| count      | int    | 是   | 条数         |

##### 3.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":[
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

**字段说明**

| 字段名    | 类型   | 说明       |
| :-------- | :----- | ---------- |
| from      | string | from地址   |
| to        | string | to地址     |
| value     | string | 余额       |
| valueName | string |            |
| fee       | string | 手续费     |
| feeName   | string | 手续费币种 |
| txHash    | string | hash       |
| blockN    | string | 高度       |
| timeStamp | string |            |
| memo      | string | 备注       |
| conAddr   | string | 合约地址   |
| status    | string | 交易状态   |



**返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "查询失败",
    "result":{}
}
```



### 3.托管云钱包管理

#### 1.获取已登录账户

##### 1.1 方法原型

 -(NSString \*)loggedAccount;

##### 1.2 返回结果

**示例：返回结果-空字符串即表示未登录**

```java
return @"+86139***";
```



#### 2.获取验证码

##### 2.1 方法原型

 -(void)getCode:(NSString \*)account finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名  | 类型   | 必须 | 说明                                                         |
| ------- | ------ | ---- | ------------------------------------------------------------ |
| account | string | 是   | 手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |

##### 2.2 返回结果

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



#### 3.登录钱包

##### 3.1 方法原型

 -(void)walletLogin:(NSString \*)account code:(NSString \*)code finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名  | 类型   | 必须 | 说明                                                         |
| ------- | ------ | ---- | ------------------------------------------------------------ |
| account | String | 是   | 手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |
| code    | String | 是   | 验证码                                                       |

##### 3.2 返回结果

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



#### 4.绑定新的验证方式

##### 4.1 方法原型

 -(void)addVerify:(NSString \*)account accountCode:(NSString \*)accountCode verifyCode:(NSString \*)verifyCode  finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名      | 类型   | 必须 | 说明                                                         |
| ----------- | ------ | ---- | ------------------------------------------------------------ |
| account     | String | 是   | 要绑定的二次验证账户，可以是手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |
| accountCode | String | 是   | 新（邮箱/手机）的验证码                                      |
| verifyCode  | String | 是   | 老（邮箱/手机）的验证码                                      |

##### 4.2 返回结果

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



#### 5.获取登录用户信息

##### 5.1 方法原型

 -(void)getUserInfoFinish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

无

##### 6.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
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

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
    "result":{}
}
```



#### 6.设置钱包支付密码

**说明：初次设置密码或忘记密码找回时调用**

##### 6.1 方法原型

 -(void)setWalletPayPwd:(NSString \*)password code:(NSString \*)code finish:(**void**(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 字段名   | 类型   | 必须 | 说明                             |
| -------- | ------ | ---- | -------------------------------- |
| password | String | 是   | 密码                             |
| code     | String | 否   | 验证码（初次设置支付密码可不传） |

##### 6.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
}
```



#### 7.修改钱包支付密码

##### 7.1 方法原型

 -(void)updateWalletPayPwd:(NSString \*)oldPwd newPwd:(NSString \*)newPwd finish:(**void**(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 字段名 | 类型   | 必须 | 说明   |
| ------ | ------ | ---- | ------ |
| oldPwd | String | 是   | 老密码 |
| newPwd | String | 是   | 新密码 |

##### 7.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
}
```



#### 8.创建云钱包

##### 8.1 方法原型

 -(void)createCloudWalletFinish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

无

##### 8.2 返回结果

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



#### 9.获取云钱包地址列表

##### 9.1 方法原型

 -(void)getCloudWalletListFinish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

无

##### 9.2 返回结果

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



#### 10.构造并签名交易

##### 10.1 方法原型

 -(void)cloudWalletTransation:(NSString \*)walletAddr password:(NSString \*)password broadcast:(BOOL)broadcast walletCall:(NSString \*)walletCall finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| walletAddr | String | 是   | 钱包地址                                                     |
| password   | String | 是   | 支付密码                                                     |
| broadcast  | bool   | 是   | 是否发送交易（true为钱包后台发送交易）                       |
| walletCall | String | 是   | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |

##### 8.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
    "result": {
        "tx":"4629F91DD3D6...473BCEF3EE91E750D",
		"hash": "4629F91DD3D6...473BCEF3EE91E750D"
    }
}

```

**字段说明**

| 字段名 | 类型   | 说明             |
| ------ | ------ | ---------------- |
| tx     | String | 已签名的交易数据 |
| hash   | string | 交易hash         |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
    "result":{}
}
```



#### 11.数据签名

##### 11.1 方法原型

 -(void)signData:(NSString \*)walletAddr password:(NSString \*)password tbsData:(NSArray \*)tbsData finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| walletAddr | String | 是   | 钱包地址                                                     |
| password   | String | 是   | 支付密码                                                     |
| tbsData    | Array  | 是   | 待签名数据列表，item为hexstring (例：["23D464F3BF...C3442247FE5E625A","C9D464F3BF...C3442247FE5E625A"]) |

##### 11.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
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

**字段说明**

| 字段名     | 类型   | 说明                              |
| ---------- | ------ | --------------------------------- |
| signpubKey | String | 签名数据的私钥对应的公钥          |
| signature  | array  | 签名后的数据，格式为Hexstring数组 |

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
    "result":{}
}
```



#### 12.退出登录

##### 12.1 方法原型

 -(void)logoutFinish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

无

##### 12.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
}
```

