## IOS托管钱包SDK接口文档说明



### 版本&更新记录

| 版本号  | 作者        | 日期       | 更新内容                      |
| ------- | ----------- | ---------- | ----------------------------- |
| v.1.0.0 | cloudwallet | 2020-06-16 | 初始版本                      |
| v.1.0.1 | cloudwallet | 2020-06-29 | 新增OTC模块                   |
| v.1.0.2 | cloudwallet | 2020-07-23 | 新增OTC卖币及USDT代收付款功能 |

------

------



### 功能说明

本文档提供托管钱包的SDK访问接口说明。IOS版本。



### 接口访问方式

API调用，返回的内容也是一个json串，里面会携带返回的状态 码以及一些返回的必要参数。



### 统一状态码

| code | 描述                                    |
| ---- | --------------------------------------- |
| 0    | 成功                                    |
| 1001 | 无效token（需重新登录）                 |
| 1002 | 无效时间戳                              |
| 1003 | 无效链类型                              |
| 1004 | 无效appId                               |
| 1005 | 无效商户                                |
| 1006 | appId和apiKey不匹配                     |
| 1007 | 验证码不正确                            |
| 1008 | 参数不能为空                            |
| 1009 | 账户已被绑定                            |
| 1010 | 格式不正确                              |
| 1011 | 无效地址                                |
| 1012 | 参数过长,不能超过                       |
| 1013 | 免密支付已过期（需重新开启免密授权）    |
| 2000 | 系统异常                                |
| 2001 | 不支持的支付方式                        |
| 2100 | 不支持的银行卡                          |
| 2101 | 银行卡号已被绑定                        |
| 2102 | 未找到绑定的银行卡                      |
| 2103 | 银行卡号无效                            |
| 3000 | 系统异常                                |
| 3001 | 账号或密码不正确                        |
| 3002 | 无效的手机号码                          |
| 3003 | 无效的邮箱                              |
| 3004 | 换绑邮箱需要先绑定手机                  |
| 3005 | 换绑手机需要先绑定邮箱                  |
| 3006 | 免密支付时长必须在(30分钟~1天)          |
| 3007 | 邮箱已被绑定                            |
| 3008 | 手机号已被绑定                          |
| 3100 | 发送验证码失败                          |
| 3101 | 验证码不正确                            |
| 3102 | 新账号的验证码不正确                    |
| 3103 | 原账号的验证码不正确,或者账户信息已过期 |
| 3200 | 密码不合法                              |
| 3201 | 密码不正确                              |
| 3202 | 原密码不正确                            |
| 3203 | 原密码和新密码不能一致                  |
| 3204 | 请先设置支付密码                        |
| 3205 | 请先设置登录密码                        |
| 4000 | 系统异常                                |
| 4001 | 付款金额和购买币种数量不能同时为空      |
| 4002 | 支付金额无效                            |
| 4003 | 币种数量无效                            |
| 4004 | 获得金额无效                            |
| 4011 | 获取汇率异常                            |
| 4012 | 每页数量太大                            |
| 4013 | 待签名数据不能为空                      |
| 4014 | 地址已被冻结,暂时无法转账               |
| 4015 | 不能给自己转账                          |
| 4016 | 地址余额不足                            |
| 4017 | 手续费不足                              |
| 4018 | 转账异常                                |
| 4101 | 下单失败                                |
| 4102 | 订单Id不能重复                          |
| 4103 | 订单已失效                              |
| 5000 | 系统异常                                |
| 5001 | 不支持的链类型                          |
| 5002 | 不支持的币种类型                        |
| 5003 | 无效的合约方法                          |
| 5004 | 地址不合法                              |
| 5005 | 合约地址无效                            |
| 9000 | 系统内部错误                            |
| 9001 | 系统异常，请联系客服处理                |
| 9002 | 无法识别的错误码，请联系客服处理        |

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

##### 2.1 方法原型

\-(BOOL)setChainType:(NSString \*)chainType;

 **输入参数说明**

| 参数名    | 类型   | 必须 | 说明                                   |
| --------- | ------ | ---- | -------------------------------------- |
| chainType | string | 是   | 链类型（例：BCB、BCBJF、BCBTJF......） |

##### 2.2 返回结果

**示例：返回结果-设置成功**

```java
return YES;
```

**示例：返回结果-设置失败**

```java
return NO;
```



#### 3.设置网络超时时间

##### 3.1 方法原型

\-(BOOL)setTimeout:(NSInteger)timeout;

 **输入参数说明**

| 参数名  | 类型 | 必须 | 说明                 |
| ------- | ---- | ---- | -------------------- |
| timeout | int  | 是   | 超时时间（单位：秒） |

##### 3.2 返回结果

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

 -(void)getAssetsList:(void(^)(ICSDKResultModel * result))finish;

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
    "code":1011,
	"msg": "无效地址"
}
```



#### 2.查询指定币种余额

##### 2.1 方法原型

 -(void)getCoinDeatil:(NSString \*)walletAddr conAddr:(NSString \*)conAddr onChain:(BOOL)onChain finish:(void(^)(ICSDKResultModel * result))finish;

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
    "code":1011,
	"msg": "无效地址"
}
```



#### 3.查询指定币种交易记录

##### 3.1 方法原型

 -(void)getCoinTransactionRecord:(NSString \*)walletAddr conAddr:(NSString \*)conAddr page:(NSInteger)page count:(NSInteger)count finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                                 |
| ---------- | ------ | ---- | ---------------------------------------------------- |
| walletAddr | string | 是   | 钱包地址                                             |
| conAddr    | string | 否   | 币种合约地址（传空即为查询当前地址所有币种交易记录） |
| page       | int    | 是   | 页码从1开始                                          |
| count      | int    | 是   | 条数                                                 |

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
    "code":1011,
	"msg": "无效地址"
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
    "code":1008,
	"msg": "参数不能为空"
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
    "code":1008,
	"msg": "参数不能为空"
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
    "code":1008,
	"msg": "参数不能为空"
}
```



#### 5.获取登录用户信息

##### 5.1 方法原型

 -(void)getUserInfo:(void(^)(ICSDKResultModel * result))finish;

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
        "defaultAccount": "",
        "createTime": "",
        "lastTime": ""
    }
}

```

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
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
    "code":1001,
	"msg": "无效token",
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
    "code":1008,
	"msg": "参数不能为空"
}
```



#### 8.创建云钱包

##### 8.1 方法原型

 -(void)createCloudWallet:(void(^)(ICSDKResultModel * result))finish;

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
    "code":1008,
	"msg": "参数不能为空"
}
```



#### 9.获取云钱包地址列表

##### 9.1 方法原型

 -(void)getCloudWalletList:(void(^)(ICSDKResultModel * result))finish;

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
    "code":1001,
	"msg": "无效token"
}
```



#### 10.构造并签名交易

##### 10.1 方法原型

 -(void)cloudWalletTransation:(NSString \*)walletAddr password:(NSString \*)password broadcast:(BOOL)broadcast contract:(NSString *)contract walletCall:(NSString \*)walletCall finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| walletAddr | String | 是   | 钱包地址                                                     |
| password   | String | 是   | 支付密码(开启免密支付时可传空串)                             |
| broadcast  | bool   | 是   | 是否发送交易（true为钱包后台发送交易）                       |
| contract   | String | 否   | 查询余额的代币合约地址（可传空串）                           |
| walletCall | String | 是   | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |

##### 8.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
    "result": {
        "tx":"4629F91DD3D6...473BCEF3EE91E750D",
		"hash": "4629F91DD3D6...473BCEF3EE91E750D",
        "balance": ""
    }
}

```

**字段说明**

| 字段名  | 类型   | 说明                         |
| ------- | ------ | ---------------------------- |
| tx      | String | 已签名的交易数据             |
| hash    | String | 交易hash                     |
| balance | String | 构造交易前对应contract的余额 |

**示例：返回结果-错误时**

```java
{
    "code":1008,
	"msg": "参数不能为空"
}
```



#### 11.数据签名

##### 11.1 方法原型

 -(void)cloudWalletSignData:(NSString \*)walletAddr password:(NSString \*)password tbsData:(NSArray \*)tbsData finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 字段名     | 类型   | 必须 | 说明                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| walletAddr | String | 是   | 钱包地址                                                     |
| password   | String | 是   | 支付密码(开启免密支付时可传空串)                             |
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
    "code":1008,
	"msg": "参数不能为空"
}
```



#### 12.退出登录

##### 12.1 方法原型

 -(void)logout:(void(^)(ICSDKResultModel * result))finish;

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
    "code":1001,
	"msg": "无效token"
}
```



#### 13.获取当前免密支付状态

##### 1.1 方法原型

\-(BOOL)getSecretFreePaymentStatus;

 **输入参数说明**

无

##### 1.2 返回结果

**示例：返回结果-已开启**

```java
return YES;
```

**示例：返回结果-未开启/已失效**

```java
return NO;
```



#### 14.请求免密支付授权

##### 14.1 方法原型

 -(void)setSecretFreePayment:(NSString \*)password time:(NSInteger)time finish:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 字段名   | 类型   | 说明                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| password | String | 支付密码                                                     |
| time     | int    | 请求免密支付的时长，单位是秒(最小：1800， 默认：3600，最大：86400‬) |

##### 14.2 返回结果

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
    "code":1001,
	"msg": "无效token"
}
```



#### 15.取消免密支付授权

##### 15.1 方法原型

 -(void)cancelSecretFreePayment:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

无

##### 15.2 返回结果

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
    "code":1001,
	"msg": "无效token"
}
```



#### 16.修改用户信息

##### 16.1 方法原型

 -(void)updateUserInfo:(NSString \*)userName memo:(NSString \*)memo defaultAccount:(NSString \*)defaultAccount finish:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 字段名         | 类型   | 必传 | 说明         |
| -------------- | ------ | ---- | ------------ |
| userName       | string | 否   | 用户名昵称   |
| memo           | string | 否   | 用户备注     |
| defaultAccount | string | 否   | 默认收款账号 |

##### 16.2 返回结果

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
    "code":1001,
	"msg": "无效token"
}
```



#### 17.查询用户收款信息

##### 17.1 方法原型

 -(void)queryUserReceipt:(NSString \*)payWay finish:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 字段名 | 类型   | 必传 | 说明                                                         |
| ------ | ------ | ---- | ------------------------------------------------------------ |
| payWay | string | 否   | 收款方式（1.不传表示获取所有收款方式；2.类型有：AliPay，WechatPay，InternetBank，AlipayBankcard） |

##### 17.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result": [
        {
            "id": 123,
            "payWay": "AliPay",
            "account": "top",
            "qr": "xx",
            "holder": "xxx",
            "belongTo": "",
            "subBelongTo": "",
            "createTime":"2020-06-29 12:00:00",
            "lastTime": "2020-06-29 12:00:00",
        }
    ]
}

```

**返回参数说明**

| 参数        | 类型   | 描述                                                      |
| ----------- | ------ | --------------------------------------------------------- |
| id          | int    | 数据库id                                                  |
| payWay      | string | 收款类型(AliPay，WechatPay，InternetBank，AlipayBankcard) |
| account     | string | 账号信息                                                  |
| qr          | string | 二维码对应的字符串，不是二维码图片                        |
| holder      | string | 收款人姓名                                                |
| belongTo    | string | 支付机构                                                  |
| subBelongTo | string | 支付子机构                                                |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 18.用户添加收款信息

##### 18.1 方法原型

 -(void)addUserReceipt:(NSString \*)payWay account:(NSString \*)account qr:(NSString \*)qr holder:(NSString \*)holder belongTo:(NSString \*)belongTo subBelongTo:(NSString \*)subBelongTo finish:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 参数        | 类型   | 必传 | 描述                                                      |
| ----------- | ------ | ---- | --------------------------------------------------------- |
| payWay      | string | 是   | 收款类型(AliPay，WechatPay，InternetBank，AlipayBankcard) |
| account     | string | 是   | 账号信息                                                  |
| qr          | string | 否   | 二维码对应的字符串，不是二维码图片                        |
| holder      | string | 是   | 收款人姓名                                                |
| belongTo    | string | 否   | 支付机构 （payWay=InternetBank时，不能为空）              |
| subBelongTo | string | 否   | 支付子机构（payWay=InternetBank时，不能为空）             |

##### 18.2 返回结果

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
    "code":1001,
	"msg": "无效token"
}
```



#### 19.用户删除收款信息

##### 19.1 方法原型

 -(void)deleteUserReceipt:(NSInteger)receiptID finish:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 参数      | 类型 | 必传 | 描述         |
| --------- | ---- | ---- | ------------ |
| receiptID | int  | 是   | 收款数据库id |

##### 19.2 返回结果

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
    "code":1001,
	"msg": "无效token"
}
```



#### 20.获取支持的银行

##### 20.1 方法原型

 -(void)querySupportBanks:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

无

##### 20.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":[
    	"工商银行"
    ]
}

```

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



### 4.OTC买币

#### 1.买币预下单

##### 1.1 方法原型

 -(void)otcBuyCoinAdvance:(NSString \*)tokenType payAmount:(NSString \*)payAmount recvAmount:(NSString \*)recvAmount recvAddr:(NSString \*)recvAddr payWay:(NSString \*)payWay userName:(NSString \*)userName orderId:(NSString \*)orderId finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数       | 类型   | 必传 | 描述                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| tokenType  | string | 是   | 需要购买的币种类型（当前支持币种：BCB、DC）                  |
| payAmount  | string | 否   | 付款金额                                                     |
| recvAmount | string | 否   | 获取币种数量(payAmount和recvAmount二选一,另一字段传nil或空串) |
| recvAddr   | string | 是   | 收款地址                                                     |
| payWay     | string | 是   | 支付（AliPay，WechatPay）                                    |
| userName   | string | 否   | 当payWay是InternetBank的时候为必填项目                       |
| orderId    | string | 是   | 订单Id                                                       |

##### 1.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "expireTime":1576814400,
		"orderId":"oewifjfj8342093r",
		"recvAmount":50.0,
		"payAmount":1000.0,
		"rate":0.05
    }
}

```

**字段说明**

| 字段名     | 类型    | 说明     |
| ---------- | ------- | -------- |
| expireTime | long    | 过期时间 |
| orderId    | string  | 订单Id   |
| recvAmount | decimal | 购买数量 |
| payAmount  | decimal | 支付数量 |
| rate       | decimal | 汇率     |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 2.买币确认下单

##### 2.1 方法原型

 -(void)otcBuyCoinConfirm:(NSString *)orderId finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数    | 类型   | 必传 | 描述   |
| ------- | ------ | ---- | ------ |
| orderId | string | 是   | 订单Id |

##### 2.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok"
}

```

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 3.查询买币订单详情

##### 3.1 方法原型

 -(void)otcOrderDetails:(NSString *)orderId finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数    | 类型   | 必传 | 描述   |
| ------- | ------ | ---- | ------ |
| orderId | string | 是   | 订单Id |

##### 3.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "orderId": "TB01200204091426074b647c0aacaa04e40a363a11a679a8127",
        "tokenType": "DC",
        "payAmount": 10.0,
        "payWay": "AliPay",
        "recvAmount": 10.0,
        "recvAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "rate": 0,
        "fee": "",
        "status": 0, //创建(0),匹配中(10),交易中(20),已付款(25),已收款(30),已取消(40),已完成(100)
        "expired": 1589971203987,
        "createTime":"2020-06-29 12:00:00",
        "lastTime":"2020-06-29 13:00:00",
        "pay":{
            "qr": "",
            "account":"wxp://f2f0A552Rsvyz-HoycPWEfXqxNobtqx8-1Go",
			"payWay":"WechatPay",
			"holder":"无名氏",
			"belongTo":"微信支付",
            "subBelongTo": "",
			"status":3,
			"expired":1589971203987
        }
    }
}

```

**字段说明**

| 参数           | 类型    | 描述                                                         |
| -------------- | ------- | ------------------------------------------------------------ |
| orderId        | string  | 订单编号                                                     |
| payAmount      | decimal | 支付数量                                                     |
| payWay         | string  | 支付方式，AliPay，WechatPay                                  |
| tokenType      | string  | 换得币种                                                     |
| recvAmount     | decimal | 换得数量                                                     |
| recvAddr       | string  | 接收币的地址                                                 |
| rate           | decimal | 锁定汇率                                                     |
| fee            | decimal | 用户总手续费，单位：CNY                                      |
| status         | int     | 订单状态。<br>创建(0),匹配中(10),交易中(20),已取消(40),已完成(100) |
| pay            | object  | 支付信息                                                     |
| -- qr          | string  | 微信或支付宝的付款二维码                                     |
| -- account     | string  | 收款账户                                                     |
| -- payWay      | string  | 支付方式，AliPay，WechatPay                                  |
| -- holder      | string  | 收款人实名                                                   |
| -- belongTo    | string  | 支付机构                                                     |
| -- subBelongTo | string  | 支付机构子机构                                               |
| -- status      | int     | 金钻订单状态<br>1：已创建<br/>2：已接单<br/>3：已完成<br/>4：已取消<br/>5：批发商已付款 |
| -- expired     | long    | 本阶段超时时间戳                                             |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 4.查询买币订单记录

##### 4.1 方法原型

 -(void)otcOrderRecords:(NSString *)address page:(NSInteger)page count:(NSInteger)count finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数    | 类型   | 必传 | 描述                                   |
| ------- | ------ | ---- | -------------------------------------- |
| address | string | 否   | 钱包地址（传空即为当前账号下订单记录） |
| page    | int    | 是   | 页码从1开始                            |
| count   | int    | 是   | 条数                                   |

##### 4.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "info": {
			"page": 4,
			"totalpage": 401,
			"count": 50,
			"total": 20034
		},
		"list": [{
            "orderId": "TB01200204091426074b647c0aacaa04e40a363a11a679a8127",
			"tokenType": "DC",
            "chainType": "BCB",
			"payAmount": 10.0,
			"payWay": "AliPay", //（AliPay，WechatPay）
			"recvAmount": 10.0,
            "recvAddr": "",
            "rate": 0,
            "fee": "",
            "txHash": "",
            "status": 0, //创建(0),匹配中(10),交易中(20),已付款(25), 已收款(30),已取消(40),已完成(100)
			"expired": 1589971203987,
            "createTime":"2020-06-29 12:00:00",
        	"lastTime":"2020-06-29 13:00:00"
		}]
    }
}

```

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 5.查询买币汇率

##### 5.1 方法原型

 -(void)otcBuyCoinRate:(NSString *)tokenType finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数      | 类型   | 必传 | 描述               |
| --------- | ------ | ---- | ------------------ |
| tokenType | string | 否   | 需要购买的币种类型 |

##### 5.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "rates":{
            "BTC":{                    // gotCoin
            	"accuracy":4,
                "channel":{            // 支付通道
                	"AliPay":{         // 通道类型
                        "min":0.1,    // 最小下单量，以此币种为单位
                        "max":11000,    // 最大下单量，以此币种为单位
                        "rate":0.022    //1 CNY = rate gotCoin
                    },
                    "WechatPay":{
                        "min":0.09,
                        "max":19000,
                        "rate":0.022
                    },
                    "InternetBank":{
                        "min":0.08,
                        "max":18000,
                        "rate":0.022
                    },
                    "AlipayBankcard":{
                        "min":0.02,
                        "max":20000,
                        "rate":0.022
                    }
                }
            }
		}
    }
}

```

**字段说明**

| 参数     | 类型    | 描述               |
| -------- | ------- | ------------------ |
| accuracy | int     | 支持购买币种的精度 |
| min      | decimal | 币种最小购买数量   |
| max      | decimal | 币种最大购买数量   |
| rate     | decimal | 汇率               |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 6.一步式直接买币下单

##### 6.1 方法原型

 -(void)otcBuyCoinImmediate:(NSString \*)tokenType payAmount:(NSString \*)payAmount recvAmount:(NSString \*)recvAmount recvAddr:(NSString \*)recvAddr payWay:(NSString \*)payWay userName:(NSString *)userName finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数       | 类型   | 必传 | 描述                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| tokenType  | string | 是   | 需要购买的币种类型（当前支持币种：BCB、DC）                  |
| payAmount  | string | 否   | 付款金额                                                     |
| recvAmount | string | 否   | 获取币种数量(payAmount和recvAmount二选一,另一字段传nil或空串) |
| recvAddr   | string | 是   | 收款地址                                                     |
| payWay     | string | 是   | 支付方式（AliPay，WechatPay）                                |
| userName   | string | 否   | 当payWay是InternetBank的时候为必填项目                       |

##### 6.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "orderId":"IW20200629153028yw349j"
    }
}

```

**字段说明**

| 字段名  | 类型   | 说明   |
| ------- | ------ | ------ |
| orderId | string | 订单Id |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 7.获取买币资产列表

##### 7.1 方法原型

 -(void)otcBuyCoinAssets:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

无

##### 7.2 返回结果

**示例：返回结果-正确时**

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

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 8.买币我已付款

##### 8.1 方法原型

 -(void)otcBuyCoinOrderPaid:(NSString \*)orderId finish:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 参数    | 类型   | 必传 | 描述   |
| ------- | ------ | ---- | ------ |
| orderId | string | 是   | 订单Id |

##### 8.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok"
}

```

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 9.取消买币下单

##### 9.1 方法原型

 -(void)otcBuyCoinOrderCancel:(NSString \*)orderId reason:(NSString \*)reason finish:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 参数    | 类型   | 必传 | 描述     |
| ------- | ------ | ---- | -------- |
| orderId | string | 是   | 订单Id   |
| reason  | string | 否   | 取消原因 |

##### 9.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok"
}

```

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



### 5.OTC卖币

#### 1.卖币预下单

##### 1.1 方法原型

 -(void)otcSellCoinAdvance:(NSString \*)tokenType payAmount:(NSString \*)payAmount recvAmount:(NSString \*)recvAmount receiptAccount:(NSString \*)receiptAccount refundAddr:(NSString \*)refundAddr payWay:(NSString \*)payWay orderId:(NSString \*)orderId finish:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 参数           | 类型   | 必传 | 描述                                                        |
| -------------- | ------ | ---- | ----------------------------------------------------------- |
| tokenType      | string | 是   | 需要卖出的币种类型                                          |
| payAmount      | string | 否   | 付款币种数量                                                |
| recvAmount     | string | 否   | 获取法币数量(payAmount和recvAmount二选一,另一字段传空串)    |
| receiptAccount | string | 是   | 收款账号                                                    |
| refundAddr     | string | 是   | 卖币失败的时候币种的退款地址                                |
| payWay         | string | 是   | 支付方式（AliPay，WechatPay，InternetBank，AlipayBankcard） |
| orderId        | string | 是   | 卖币订单Id                                                  |

##### 1.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "expireTime":1576814400,
		"orderId":"oewifjfj8342093r",
		"recvAmount":50.0,
		"payAmount":1000.0,
		"rate":0.05
    }
}

```

**字段说明**

| 字段名     | 类型    | 说明     |
| ---------- | ------- | -------- |
| expireTime | long    | 过期时间 |
| orderId    | string  | 订单Id   |
| recvAmount | decimal | 购买数量 |
| payAmount  | decimal | 支付数量 |
| rate       | decimal | 汇率     |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 2.卖币确认下单

##### 2.1 方法原型

 -(void)otcSellCoinConfirm:(NSString *)orderId finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数    | 类型   | 必传 | 描述   |
| ------- | ------ | ---- | ------ |
| orderId | string | 是   | 订单Id |

##### 2.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "expired":1576814400,
		"payAddress":"0x74C1b1E54E27Dd2FB5A11DB01177c94356CacB45",
		"payMemo": ""
    }
}

```

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 3.查询卖币订单详情

##### 3.1 方法原型

 -(void)otcSellCoinOrderDetails:(NSString *)orderId finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数    | 类型   | 必传 | 描述   |
| ------- | ------ | ---- | ------ |
| orderId | string | 是   | 订单Id |

##### 3.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "orderId": "IW01200204091426074b647c0aa",
        "tokenType": "DC",
        "payAmount": 10.0,
        "actualPayAmount": 10.0,
        "payWay": "InternetBank",
        "recvAmount": 10.0,
        "refundAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "payAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "rate": 0,
        "fee": "",
        "status": 0, //创建(0),交易中(20),已取消(40),已完成(100)
        "remark": "", 
        "createTime":"2020-06-29 12:00:00",
        "lastTime":"2020-06-29 13:00:00",
        "pay":{
            "qr": "",
            "account":"wxp://f2f0A552Rsvyz-HoycPWEfXqxNobtqx8-1Go",
			"payWay":"WechatPay",
			"holder":"无名氏",
			"belongTo":"微信支付",
            "subBelongTo": "",
			"status":3 //金钻订单状态1：已创建,3：已完成，4：已取消
        }
    }
}

```

**字段说明**

| 参数           | 类型    | 描述                                                      |
| -------------- | ------- | --------------------------------------------------------- |
| orderId        | string  | 订单编号                                                  |
| payAmount      | decimal | 卖出币种的数量                                            |
| payWay         | string  | 支付方式，AliPay，WechatPay，InternetBank，AlipayBankcard |
| tokenType      | string  | 卖出的币种                                                |
| recvAmount     | decimal | 换得法币的数量                                            |
| refundAddr     | string  | 卖币失败接收退币的地址                                    |
| payAddr        | string  | 币种充值地址（卖出的币种充值到这个地址上）                |
| rate           | decimal | 锁定汇率                                                  |
| fee            | decimal | 用户总手续费，单位：CNY                                   |
| status         | int     | 订单状态。<br>创建(0),交易中(20),已取消(40),已完成(100)   |
| pay            | object  | 支付信息                                                  |
| -- qr          | string  | 微信或支付宝的付款二维码                                  |
| -- account     | string  | 收款账户                                                  |
| -- payWay      | string  | 支付方式，AliPay，WechatPay                               |
| -- holder      | string  | 收款人实名                                                |
| -- belongTo    | string  | 支付机构                                                  |
| -- subBelongTo | string  | 支付机构子机构                                            |
| -- status      | int     | 金钻订单状态<br>1：已创建<br/>3：已完成<br/>4：已取消     |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 4.查询卖币订单记录

##### 4.1 方法原型

 -(void)otcSellCoinOrderRecords:(NSInteger)page count:(NSInteger)count finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数  | 类型 | 必传 | 描述        |
| ----- | ---- | ---- | ----------- |
| page  | int  | 是   | 页码从1开始 |
| count | int  | 是   | 条数        |

##### 4.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "info": {
			"page": 4,
			"totalpage": 401,
			"count": 50,
			"total": 20034
		},
		"list": [{
            "orderId": "IW01200204091426074b647",
			"tokenType": "DC",
            "chainType": "BCB",
			"payAmount": 10.0,
            "actualPayAmount": 10.0,
        	"refundAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            "payAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
			"payWay": "InternetBank", //（AliPay，WechatPay,InternetBank）
            "receiptAccount": "123",
			"recvAmount": 10.0,
            "remark": "123",
            "rate": 0,
            "fee": "",
            "status": 0, //创建(0),交易中(20),已取消(40),已完成(100)
			"expired": 1589971203987,
            "createTime": "2020-06-29 12:00:00",
            "lastTime": "2020-06-29 12:00:00"
		}]
    }
}

```

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 5.查询卖币汇率

##### 5.1 方法原型

 -(void)otcSellCoinRate:(NSString *)tokenType finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数      | 类型   | 必传 | 描述     |
| --------- | ------ | ---- | -------- |
| tokenType | string | 否   | 币种类型 |

##### 5.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "rates":{
            "BTC":{                    // gotCoin
            	"accuracy":4,
                "channel":{            // 支付通道
                	"AliPay":{         // 通道类型
                        "min":0.1,    // 最小下单量，以此币种为单位
                        "max":11000,    // 最大下单量，以此币种为单位
                        "rate":0.022    //1 CNY = rate gotCoin
                    },
                    "WechatPay":{
                        "min":0.09,
                        "max":19000,
                        "rate":0.022
                    },
                    "InternetBank":{
                        "min":0.08,
                        "max":18000,
                        "rate":0.022
                    },
                    "AlipayBankcard":{
                        "min":0.02,
                        "max":20000,
                        "rate":0.022
                    }
                }
            }
		}
    }
}

```

**字段说明**

| 参数     | 类型    | 描述               |
| -------- | ------- | ------------------ |
| accuracy | int     | 支持购买币种的精度 |
| min      | decimal | 币种最小购买数量   |
| max      | decimal | 币种最大购买数量   |
| rate     | decimal | 汇率               |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 6.一步式卖币下单

##### 6.1 方法原型

 -(void)otcSellCoinImmediate:(NSString *)tokenType payAmount:(NSString *)payAmount recvAmount:(NSString *)recvAmount receiptAccount:(NSString *)receiptAccount refundAddr:(NSString *)refundAddr payWay:(NSString *)payWay finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数           | 类型   | 必传 | 描述                                                         |
| -------------- | ------ | ---- | ------------------------------------------------------------ |
| tokenType      | string | 是   | 需要购买的币种类型（当前支持币种：BCB、DC）                  |
| payAmount      | string | 否   | 付款金额                                                     |
| recvAmount     | string | 否   | 获取币种数量(payAmount和recvAmount二选一,另一字段传nil或空串) |
| receiptAccount | string | 是   | 收款地址                                                     |
| refundAddr     | string | 是   | 卖币失败的时候币种的退款地址                                 |
| payWay         | string | 是   | 支付方式（AliPay，WechatPay）                                |

##### 6.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "orderId":"IW20200629153028yw349j",
        "expired":1576814400,
		"payAddress":"0x74C1b1E54E27Dd2FB5A11DB01177c94356CacB45",
		"payMemo": ""
    }
}

```

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 7.获取卖币资产列表

##### 7.1 方法原型

 -(void)otcSellCoinAssets:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

无

##### 7.2 返回结果

**示例：返回结果-正确时**

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

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



### 6.USDT代收付款

#### 1.校验币种地址

##### 1.1 方法原型

 -(void)usdtVerifyAddress:(NSString \*)address tokenType:(NSString \*)tokenType finish:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

| 参数      | 类型   | 必传 | 描述     |
| --------- | ------ | ---- | -------- |
| address   | string | 是   | 地址     |
| tokenType | string | 是   | 币种类型 |

##### 1.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "verify": true
    }
}

```

**字段说明**

| 字段名 | 类型 | 说明     |
| ------ | ---- | -------- |
| verify | bool | 校验结果 |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 2.获取USDT代收款币种

##### 2.1 方法原型

 -(void)usdtReceiptCoins:(void(^)(ICSDKResultModel \* result))finish;

**参数字段说明**

无

##### 2.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":[{
	   	"tokenType":"USDTERC",
        "displayName": "ERC20",
        "fee":0,
        "rate":1,
        "accuracy":4,
        "min":1,
        "max":10000,
	},{
        "tokenType":"USDTOmni",
        "displayName": "OMNI",
        "fee":1,
        "rate":1,
        "accuracy":4,
        "min":10,
        "max":10000,
	}]
}

```

| 参数        | 类型    | 描述                          |
| ----------- | ------- | ----------------------------- |
| tokenType   | string  | 代收款币种                    |
| displayName | string  | 显示名称                      |
| fee         | decimal | 手续费                        |
| rate        | decimal | 汇率1 tokenType = rate USD    |
| accuracy    | int     | 精度                          |
| min         | decimal | 最小兑换限额，币种：tokenType |
| max         | decimal | 最大兑换限额，币种：tokenType |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 3.获取USDT代收款地址

##### 3.1 方法原型

 -(void)usdtReceiptAddress:(NSString *)address tokenType:(NSString *)tokenType finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数      | 类型   | 必传 | 描述       |
| --------- | ------ | ---- | ---------- |
| address   | string | 是   | 充值地址   |
| tokenType | string | 是   | 代充值币种 |

##### 3.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "tokenType": "USDTERC",
		"addr":"0xcb39ac3ecf3e69fcbb33b9f62df30c4f41f6a62d",
		"memo": ""
    }
}

```

**字段说明**

| 参数      | 类型   | 描述                 |
| --------- | ------ | -------------------- |
| tokenType | string | 代收款币种           |
| addr      | string | 代收款币种对应的地址 |
| memo      | string | 地址备注             |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 4.获取USDT代付款币种

##### 4.1 方法原型

 -(void)usdtPaymentCoins:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

无

##### 4.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":[{
	   	"tokenType":"USDTERC",
        "displayName": "ERC20",
        "fee":0,
        "rate":1,
        "accuracy":4,
        "min":1,
        "max":10000,
	},{
        "tokenType":"USDTOmni",
        "displayName": "OMNI",
        "fee":1,
        "rate":1,
        "accuracy":4,
        "min":10,
        "max":10000,
	}]
}

```

| 参数        | 类型    | 描述                          |
| ----------- | ------- | ----------------------------- |
| tokenType   | string  | 代付款币种                    |
| displayName | string  | 显示名称                      |
| fee         | decimal | 手续费                        |
| rate        | decimal | 汇率1 tokenType = rate USD    |
| accuracy    | int     | 精度                          |
| min         | decimal | 最小兑换限额，币种：tokenType |
| max         | decimal | 最大兑换限额，币种：tokenType |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 5.获取USDT代付款地址

##### 5.1 方法原型

 -(void)usdtPaymentAddress:(NSString *)address tokenType:(NSString *)tokenType finish:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

| 参数      | 类型   | 必传 | 描述          |
| --------- | ------ | ---- | ------------- |
| address   | string | 是   | USDTBRC的地址 |
| tokenType | string | 是   | 代付款币种    |

##### 5.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "tokenType": "USDTOMNI",
		"addr":"bcbDPa4daKK3hfQh9Eq7W4CTuxgoGYbr4AyW",
		"memo": ""
    }
}

```

**字段说明**

| 参数      | 类型   | 描述                                   |
| --------- | ------ | -------------------------------------- |
| tokenType | string | 待付款币种                             |
| addr      | string | USDTBRC对应的回收地址                  |
| memo      | string | 地址标签（格式如下，需转成jsonString） |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```

注：

在代付款的交易中，需要填充memo字段，

memo格式协议：

```
{
	"a": "0x0615c02f3cdab714f57687ef8a0028daf983ae4c",//收款人地址
	"m":"aaa"  // 地址标签
}
```



### 7.其他接口

#### 1.获取服务器时间

##### 1.1 方法原型

 -(void)getServiceTimestamp:(void(^)(ICSDKResultModel * result))finish;

**参数字段说明**

无

##### 1.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "timeStamp":1576814400000,
    }
}

```

**字段说明**

| 字段名    | 类型 | 说明                 |
| --------- | ---- | -------------------- |
| timeStamp | long | 服务器时间戳（毫秒） |

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "其他错误"
}
```



#### 2.获取支持的链类型

##### 2.1 方法原型

 -(void)getSupportChains:(void(^)(ICSDKResultModel * result))finish;

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
            "chainType": "BCB",
            "ChainName": "BCB链"
        },
        {
            "chainType": "BCBJF",
            "ChainName": "久发链"
        }
    ]
}

```

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "其他错误"
}
```

