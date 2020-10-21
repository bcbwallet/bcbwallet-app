

## **Android托管钱包SDK接口文档说明**





### 版本&更新记录



| 版本号         | 作者 | 日期       | 更新内容                                                     |
| -------------- | ---- | ---------- | ------------------------------------------------------------ |
| v.1.0.0        | jjm  | 2020-06-16 | 初始版本                                                     |
| v.1.0.1        | jjm  | 2020-06-28 | 新增OTC买币回调和设置网络请求超时时间回调                    |
| v.1.0.2        | jjm  | 2020-06-29 | 调整5-3/5-4加了俩个字段，添加一步式直接买币，SDK内部处理订单ID，去除5-4订单ID参数 |
| 1.3.3-SNAPSHOT | jjm  | 2020-07-16 | 增加3.10签名交易 ，请求添加contract参数，返回值增加balance参数 |
| 1.4.0-SNAPSHOT | jjm  | 2020-07-24 | 1，新增OTC卖币，USDT代付接口模块 ,其他接口。                                                        2，2.3回调返回值新增bcbScanPath字段，请求参数的contract现在是可选                                                                                           3， 新增3.13,14,15,16,17,18 回调                                                                                                                                   4，5.1的请求字段payWay新增2个值InternetBank，AlipayBankcard                                                                                                                         5，5.3和5.4返回值新增txHash字段  ，5.4请求参数添加chainType字段，返     回值添加chainType字段                                                                                                                                   6，5.5接口返回值改动比较大                                                                                                                                                                                              7，5.1请求参数新增username |
| 1.5.4-SNAPSHOT | jjm  | 2020-08-4  | 添加7.6USDT代付转账                                          |
| 1.6.2-SNAPSHOT | jjm  | 2020-08-5  | 添加1.4 设置语言                                             |
| 1.7.1-SNAPSHOT | jjm  | 2020-08-20 | 添加闪兑功能                                                 |
| 1.7.6-SNAPSHOT | jjm  | 2020-09-15 | 接口2.1返回值新增depositEnabled，withdrawEnabled，displayName          新增8.7闪兑反查询汇率 |
| 1.7.8-SNAPSHOT | jjm  | 2020-10-20 | 接口2.1,6.7返回值新增tokenName，agentEnabled,agentContract,agentFee,agentFeeToken,agentMethod字段，新增接口3.19 |

------

------



### 功能说明

本文档提供托管钱包的SDK访问接口说明。ANDROID版本。



### 接口访问方式

普通方法调用的方式，以下接口都是WalletAssistant的静态方法



### 1初始化设置

#### 1.商户信息设置

##### 1.1方法原型：

boolean init(Context context,String appId,String apiKey,String domain);

 **输入参数说明**

| 参数名  | 类型    | 必须 | 说明                                                         |
| ------- | ------- | :--- | ------------------------------------------------------------ |
| context | Context | 是   | Application的Context                                         |
| appId   | string  | 是   | 云钱包后台分配的App唯一ID                                    |
| apiKey  | string  | 是   | 托管分配的密钥                                               |
| domain  | string  | 是   | 云钱包后台域名域名（例："https://api.iwallet.cloud/pkey_api"--云钱包后台） |

##### 1.2 返回结果

true：初始化成功，false：初始化失败

方法说明：

全局的初始化接口，建议在Application的onCreate中调用



#### 2.设置链

##### 2.1 方法原型

boolean setChainType(String chainType);

 **输入参数说明**

| 参数名    | 类型   | 必须 | 说明                                   |
| --------- | ------ | ---- | -------------------------------------- |
| chainType | string | 是   | 链类型（例：BCB、BCBJF、BCBTJF......） |

##### 2.2 返回结果

**示例：返回结果-设置成功**

```java
return true;
```

**示例：返回结果-设置失败**

```java
return false;
```



#### 3.设置网络超时时间

##### 3.1 方法原型

boolean setTimeout(int timeout);

 **输入参数说明**

| 参数名  | 类型 | 必须 | 说明                 |
| ------- | ---- | ---- | -------------------- |
| timeout | int  | 是   | 超时时间（单位：秒） |

##### 3.2 返回结果

**示例：返回结果-设置成功**

```java
return true;
```

**示例：返回结果-设置失败**

```java
return false;
```

#### 4.设置语言

##### 4.1 方法原型

boolean setLang(String lang);

 **输入参数说明**

| 参数名 | 类型   | 必须 | 说明                                        |
| ------ | ------ | ---- | ------------------------------------------- |
| lang   | String | 是   | 请求语言版本（默认根据IP来判断国家）"zh-CN" |

##### 4.2 返回结果

**示例：返回结果-设置成功**

```java
return true;
```

**示例：返回结果-设置失败**

```java
return false;
```



### 2.钱包地址相关信息查询

#### 1.查询默认资产列表

##### 1.1 方法原型

void getAssetsList(OnWalletListCallback callback);

**参数字段说明**

| 参数名   | 类型                 | 必须 | 说明                                                 |
| -------- | -------------------- | ---- | ---------------------------------------------------- |
| callback | OnWalletListCallback | 是   | 回调接口,见附录[13.2]()，true 成功，false 失败见附录 |

##### 1.2 返回结果

**返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
	"result":[
        {
            "tokenName": "token-basic",
            "depositEnabled": true,
            "withdrawEnabled": true,
            "displayName": "BCB",
            "symbol":"BCB",
            "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            "decimals":"9",
            "coinIcon":"http://test.6x.com/coin_icons/bcb.icon",
            "agentEnabled": false,
        },
        {
            "tokenName": "token-basic",
            "depositEnabled": true,
            "withdrawEnabled": true,
            "displayName": "BCB",
            "symbol":"USDX",
            "conAddr":"bcbMLpC7HFd8JCm6RXQiu1t7aX4GaiW5c4Cm",
            "decimals":"9",            
            "coinIcon":"http://test.6x.com/coin_icons/usdx.icon"
            "agentEnabled": true,
            "agent":{
                "agentContract": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            	"agentFee": "0.01",
                "agentFeeToken": "USDX",
                "agentMethod": "Transfer(string,types.Address,bn.Number)",
        }
    ]
}

```

**字段说明**

| 字段名          | 类型   | 说明                               |
| --------------- | ------ | ---------------------------------- |
| depositEnabled  | bool   | 充值开关                           |
| withdrawEnabled | bool   | 体现开关                           |
| displayName     | string | 展示名称                           |
| symbol          | string | 符号                               |
| conAddr         | string | 合约地址                           |
| decimals        | string | 精度                               |
| coinIcon        | string | 币种图标                           |
| tokenName       | string | 币种链上名称                       |
| agentEnabled    | bool   | 是否应该使用代付手续费合约进行转账 |
| agentContract   | string | 代付手续费合约地址                 |
| agentFee        | string | 消耗手续费                         |
| agentFeeToken   | string | 手续费币种                         |
| agentMethod     | string | 代转账方法                         |

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

**void getCoinDetail( String address,String coinAddr,boolean onChain,OnWalletCallback callback);**

**参数字段说明**

| 字段名     | 类型             | 必须 | 说明                                                 |
| ---------- | ---------------- | ---- | ---------------------------------------------------- |
| walletAddr | string           | 是   | 钱包地址                                             |
| conAddr    | string           | 是   | 币种合约地址                                         |
| onChain    | boolean          | 是   | 是否直接查询链上余额  （true为链上查询）             |
| callback   | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |



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

**void getCoinTransactionDetail(String address,String coinAddr,String contract, int page,int count,OnWalletListCallback callback);**

**参数字段说明**

| 字段名     | 类型                 | 必须 | 说明                                                 |
| ---------- | -------------------- | ---- | ---------------------------------------------------- |
| walletAddr | string               | 是   | 钱包地址                                             |
| conAddr    | string               | 是   | 币种合约地址                                         |
| contract   | string               | 是   | 合约地址,可选可不选                                  |
| page       | int                  | 是   | 页码从1开始                                          |
| count      | int                  | 是   | 条数                                                 |
| callback   | OnWalletListCallback | 是   | 回调接口,见附录[13.2]()，true 成功，false 失败见附录 |

##### 3.2 返回结果

**返回结果-正确时**

```java
{
	"code": 0,
	"message": "ok",
    "data":[
        {
            "from":"0x0ef50dd9256d872c6ddb45742dbbd927a697843a",
            "to":"0x9745120cf86659c69729182ea63c3c60a2f88101",
            "value":"3",
            "valueName":"bcb(bcbglobal)",
            "fee":"0.00036647",
            "feeName":"Ether",
			"txHash":"0x44c67f018ef2…aa2b7cce2c688c85ab75",
            "blockN":"5520922",
            "timeStamp":"1525330230",
            "memo":"",
            "conAddr":"0x9F138D5D9e24186eC96B35e5B5530C907860A78d",
            "status":"0x1"
        },
        {
            "from":"0x0ef50dd9256d872c6ddb45742dbbd927a697843a",
            "to":"0x9745120cf86659c69729182ea63c3c60a2f88101",
            "value":"3",
            "valueName":"Ether",
            "fee":"0.00036647",
            "feeName":"Ether",
            "txHash":"0x44c67f018ef2…aa2b7cce2c688c85ab75",
            "blockN":"5520922",
            "timeStamp":"1525330230",
            "memo":"",
            "conAddr":"",
            "status":"0x0"
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

Stirng loggedAccount;

##### 1.2 返回结果

**示例：返回结果-空字符串即表示未登录**

```java
return "";
```



#### 2.获取验证码

##### 2.1 方法原型

void getCode(String account, OnWalletCallback callback);

| 字段名   | 类型             | 必须 | 说明                                                         |
| -------- | ---------------- | ---- | ------------------------------------------------------------ |
| account  | string           | 是   | 手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录         |

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

void walletLogin(String account, String code, OnWalletCallback callback);

**参数字段说明**

| 字段名   | 类型             | 必须 | 说明                                                         |
| -------- | ---------------- | ---- | ------------------------------------------------------------ |
| account  | String           | 是   | 手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |
| code     | String           | 是   | 验证码                                                       |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录         |

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

void addVerify(String account, String accountCode，String verifyCode , OnWalletCallback callback);

**参数字段说明**

| 字段名      | 类型             | 必须 | 说明                                                         |
| ----------- | ---------------- | ---- | ------------------------------------------------------------ |
| account     | String           | 是   | 要绑定的二次验证账户，可以是手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |
| accountCode | String           | 是   | 新（邮箱/手机）的验证码                                      |
| verifyCode  | String           | 是   | 老（邮箱/手机）的验证码                                      |
| callback    | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录         |

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

void getUserInfo(OnWalletCallback callback);

**参数字段说明**

| 参数名   | 类型             | 必须 | 说明                                                 |
| -------- | ---------------- | ---- | ---------------------------------------------------- |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

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

void setWalletPayPwd(String password, String code, OnWalletCallback callback);

**参数字段说明**

| 字段名   | 类型             | 必须 | 说明                                                 |
| -------- | ---------------- | ---- | ---------------------------------------------------- |
| password | String           | 是   | 密码                                                 |
| code     | String           | 否   | 验证码（初次设置支付密码可不传）                     |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

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

void updateWalletPayPwd(String oldPwd, String newPwd, OnWalletCallback callback);

**参数字段说明**

| 字段名   | 类型             | 必须 | 说明                                                 |
| -------- | ---------------- | ---- | ---------------------------------------------------- |
| oldPwd   | String           | 是   | 老密码                                               |
| newPwd   | String           | 是   | 新密码                                               |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

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

void createCloudWallet(OnWalletCallback callback);

**参数字段说明**

| 参数名   | 类型             | 必须 | 说明                                                 |
| -------- | ---------------- | ---- | ---------------------------------------------------- |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

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

void getCloudWalletList( OnWalletListCallback  callback);

**参数字段说明**

| 参数名   | 类型             | 必须 | 说明                                                 |
| -------- | ---------------- | ---- | ---------------------------------------------------- |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

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

void cloudWalletTransation(String walletAddr, String password，bool broadcast, String contract, String walletCall, OnWalletCallback callback);

**参数字段说明**

| 字段名     | 类型             | 必须 | 说明                                                         |
| ---------- | ---------------- | ---- | ------------------------------------------------------------ |
| walletAddr | String           | 是   | 钱包地址                                                     |
| password   | String           | 是   | 支付密码                                                     |
| contract   | string           | 否   | 查询余额的代币合约地址                                       |
| broadcast  | bool             | 是   | 是否发送交易（true为钱包后台发送交易）                       |
| walletCall | String           | 是   | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |
| callback   | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录         |

##### 8.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "",
    "result": {
        "tx":"4629F91DD3D6...473BCEF3EE91E750D",
		"hash": "4629F91DD3D6...473BCEF3EE91E750D"
        "balance": ""
    }
}

```

**字段说明**

| 字段名  | 类型   | 说明                         |
| ------- | ------ | ---------------------------- |
| tx      | String | 已签名的交易数据             |
| hash    | string | 交易hash                     |
| balance | string | 构造交易前对应contract的余额 |

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

void cloudWalletSignData(String walletAddr, String password，String tbsData,OnWalletListCallback  callback);

**参数字段说明**

| 字段名     | 类型             | 必须 | 说明                                                         |
| ---------- | ---------------- | ---- | ------------------------------------------------------------ |
| walletAddr | String           | 是   | 钱包地址                                                     |
| password   | String           | 是   | 支付密码                                                     |
| tbsData    | Array            | 是   | 待签名数据列表，item为hexstring (例：["23D464F3BF...C3442247FE5E625A","C9D464F3BF...C3442247FE5E625A"]) |
| callback   | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录         |

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

void logout(OnWalletCallback callback);

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

#### 13.获取支持的链类型

##### 13.1 方法原型

void getSupportChains(OnWalletCallback callback)

**参数字段说明**

无

##### 14.2 返回结果

**示例：返回结果-正确时**

```java
{
	"code": 0,
	"message": "ok",
    "data":[
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

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 14.修改用户信息

##### 14.1 方法原型

void updatetUserInfo(String userName,String memo,String defaultAccount,OnWalletCallback  callback)

**参数字段说明**

| 字段名         | 类型   | 必传 | 说明         |
| -------------- | ------ | ---- | ------------ |
| userName       | string | 否   | 用户名昵称   |
| memo           | string | 否   | 用户备注     |
| defaultAccount | string | 否   | 默认收款账号 |

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



#### 15.查询用户收款信息

##### 15.1 方法原型

 void queryUserReceipt(String payWay, OnWalletListCallback  callback)

**参数字段说明**

| 字段名 | 类型   | 必传 | 说明                                                         |
| ------ | ------ | ---- | ------------------------------------------------------------ |
| payWay | string | 否   | 收款方式（1.不传表示获取所有收款方式；2.类型有：AliPay，WechatPay，InternetBank，AlipayBankcard） |

##### 15.2 返回结果

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



#### 16.用户添加收款信息

##### 16.1 方法原型

void addUserReceipt(String payWay,String account,String qr,String holder,String belongTo,String subBelongTo,OnWalletCallback  callback)

**参数字段说明**

| 参数        | 类型   | 必传 | 描述                                                      |
| ----------- | ------ | ---- | --------------------------------------------------------- |
| payWay      | string | 是   | 收款类型(AliPay，WechatPay，InternetBank，AlipayBankcard) |
| account     | string | 是   | 账号信息                                                  |
| qr          | string | 否   | 二维码对应的字符串，不是二维码图片                        |
| holder      | string | 是   | 收款人姓名                                                |
| belongTo    | string | 否   | 支付机构 （payWay=InternetBank时，不能为空）              |
| subBelongTo | string | 否   | 支付子机构（payWay=InternetBank时，不能为空）             |

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



#### 17.用户删除收款信息

##### 17.1 方法原型

 void deleteUserReceipt(String receiptID,OnWalletCallback  callback)

**参数字段说明**

| 参数      | 类型 | 必传 | 描述         |
| --------- | ---- | ---- | ------------ |
| receiptID | int  | 是   | 收款数据库id |

##### 17.2 返回结果

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



#### 18.获取支持的银行

##### 18.1 方法原型

void querySupportBanks(OnWalletListCallback  callback)

**参数字段说明**

无

##### 18.2 返回结果

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

#### 19.获取转账手续费

##### 1.1 方法原型

void getTransferFee(String tokenType,String to,String value,OnWalletCallback  callback)

**参数字段说明**

| 参数      | 类型   | 必传 | 描述     |
| --------- | ------ | ---- | -------- |
| tokenType | String | 是   | 币种类型 |
| address   | String | 是   | 地址     |
| value     | String | 否   | 转账金额 |

##### 18.2 返回结果

**示例：返回结果-正确时**

```java
 {
     "code": 0,
     "message": "ok",
     "data":{
         "fee": "0.00125",
         "feeToken": "BCB"
     }
 }

```

**参数字段说明**

| 参数     | 类型   | 必传 | 描述           |
| -------- | ------ | ---- | -------------- |
| fee      | String | 是   | 手续费         |
| feeToken | String | 是   | 手续费币种类型 |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



### 4.免密支付

#### 1.请求免密支付授权

##### 1.1 方法原型

void setSecretFreePayment(String password,String time,OnWalletListCallback  callback);

**参数字段说明**

| 字段名   | 类型             | 必须 | 说明                                                         |
| -------- | ---------------- | ---- | ------------------------------------------------------------ |
| password | string           | 是   | 支付密码                                                     |
| time     | int              | 是   | 请求免密支付的时长，单位是秒(最小：1800， 默认：3600，最大：86400‬) |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录         |

##### 1.2 返回结果

**示例：返回结果-正确时**

```java
{
	"code": 0,
	"message": "ok",
    "免密授权成功"
}

```

**示例：返回结果-错误时**

```java
{
    "code":-1001,
	"msg": "fail",
}
```

#### 2.获取当前免密支付状态

##### 2.1 方法原型

boolean getSecretFreePaymentStatus();

 **输入参数说明**

无

##### 2.2 返回结果

**示例：返回结果-已开启**

```java
return true;
```

**示例：返回结果-未开启/已失效**

```java
return false;
```

#### 3.请求取消免密支付授权

##### 3.1 方法原型

void cancelSecretFreePayment();

 **输入参数说明**

| 参数名   | 类型             | 必须 | 说明                                                 |
| -------- | ---------------- | ---- | ---------------------------------------------------- |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

##### 3.2 返回结果

**示例：返回结果-已取消

```java
return true;
```

**示例：返回结果-未开启/已失效**

```java
return false;
```

### 5.OTC模块买币

#### 1.买币预下单

##### 1.1 方法原型

 void otcBuyCoinAdvance(String tokenType,decimal payAmount,decimal recvAmount,String recvAddr,String payWay,String userName,String orderId ,OnWalletCallback callback);

**参数字段说明**

| 参数       | 类型             | 必传 | 描述                                                 |
| ---------- | ---------------- | ---- | ---------------------------------------------------- |
| tokenType  | string           | 是   | 需要购买的币种类型                                   |
| payAmount  | decimal          | 否   | 付款金额                                             |
| recvAmount | decimal          | 否   | 获取币种数量(payAmount和recvAmount二选一)            |
| recvAddr   | string           | 是   | 接收币种的地址                                       |
| payWay     | string           | 是   | 支付方式（AliPay，WechatPay）                        |
| orderId    | string           | 是   | 订单Id ，Iw年月日时分秒0-9和a-z6位随机数             |
| userName   | string           | 否   | 当payWay是InternetBank的时候为必填项目               |
| callback   | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

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

void otcBuyCoinConfirm(Stirng orderId,OnWalletCallback callback):

**参数字段说明**

| 参数     | 类型             | 必传 | 描述                                                 |
| -------- | ---------------- | ---- | ---------------------------------------------------- |
| orderId  | string           | 是   | 订单Id                                               |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

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

void otcOrderDetails(String orderId,OnWalletCallback callback);

**参数字段说明**

| 参数     | 类型             | 必传 | 描述                                                 |
| -------- | ---------------- | ---- | ---------------------------------------------------- |
| orderId  | string           | 是   | 订单Id                                               |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

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
        "rate": 0,
        "fee": "",
        "createTime" :""
        "lastTime" :""
        "status": 0, //创建(0),匹配中(10),交易中(20),已取消(40),已完成(100)
        "expired": 1589971203987,
        "pay":{
            "account":"wxp://f2f0A552Rsvyz-HoycPWEfXqxNobtqx8-1Go",
			"payWay":"WechatPay",
			"holder":"无名氏",
			"belongTo":"微信支付",
			"status":3,
			"expired":1589971203987
        }
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



#### 4.查询买币订单记录

##### 4.1 方法原型

 void otcOrderRecords(String address,int page.int count,OnWalletCallback callback);

**参数字段说明**

| 参数     | 类型             | 必传 | 描述                                                 |
| -------- | ---------------- | ---- | ---------------------------------------------------- |
| address  | string           | 是   | 钱包地址(传空即为当前账号下订单记录）                |
| page     | int              | 是   | 页码从1开始                                          |
| count    | int              | 是   | 条数                                                 |
| callback | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

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
			"payAmount": 10.0,
			"payWay": "AliPay", //（AliPay，WechatPay）
            "createTime" :""
        	"lastTime" :""
			"recvAmount": 10.0,
            "rate": 0,
            "fee": "",
            "status": 0, //创建(0),匹配中(10),交易中(20),已取消(40),已完成(100)
			"expired": 1589971203987
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

void otcBuyCoinRate(String tokenType,OnWalletCallback callback);

**参数字段说明**

| 参数      | 类型             | 必传 | 描述                                                 |
| --------- | ---------------- | ---- | ---------------------------------------------------- |
| tokenType | string           | 是   | 需要购买的币种类型                                   |
| callback  | OnWalletCallback | 是   | 回调接口,见附录[13.1]()，true 成功，false 失败见附录 |

##### 5.2 返回结果

**示例：返回结果-正确时**

```java
{
	"code": 0,
	"message": "ok",
    "data":{
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

| 参数         | 类型                    | 描述                                         |
| ------------ | ----------------------- | -------------------------------------------- |
| AliPay       | decimal                 | 使用支付宝的汇率（1CNY能购买币种的数量）     |
| WechatPay    | decimal                 | 使用微信支付的汇率（1CNY能购买币种的数量）   |
| InternetBank | decimal                 | 使用银行卡支付的汇率（1CNY能购买币种的数量） |
| accuracy     | int                     | 支持购买币种的精度                           |
| min          | decimal                 | 币种最小购买数量                             |
| max          | decimal                 | 币种最大购买数量                             |
| channel      | map<payWay, payChannel> | 每个通道的限额                               |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```

#### 6.一步式直接买币下单

##### 6.1 方法原型

 void otcBuyCoinImmediate(String tokenType,decimal payAmount,decimal recvAmount,String recvAddr,String payWay,String userName,OnWalletCallback callback);

**参数字段说明**

| 参数       | 类型    | 必传 | 描述                                                         |
| ---------- | ------- | ---- | ------------------------------------------------------------ |
| tokenType  | string  | 是   | 需要购买的币种类型（当前支持币种：BCB、DC）                  |
| payAmount  | decimal | 否   | 付款金额                                                     |
| recvAmount | decimal | 否   | 获取币种数量(payAmount和recvAmount二选一,另一字段传nil或空串) |
| recvAddr   | string  | 是   | 收款地址                                                     |
| payWay     | string  | 是   | 支付方式（AliPay，WechatPay）                                |
| userName   | string  | 否   | 当payWay是InternetBank的时候为必填项目                       |

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

void otcBuyCoinAssets(OnWalletListCallback callback);

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

#### 8.取消买币下单

##### 8.1 方法原型

void otcCancelBuyCoin(String orderId,String reason, OnWalletCallback callback);

**参数字段说明**

| 参数    | 类型   | 必传 | 描述     |
| ------- | ------ | ---- | -------- |
| orderId | string | 是   | 订单Id   |
| reason  | string | 否   | 取消原因 |

##### 8.2 返回结果

**示例：返回结果-正确时**

```java
{
	"code": 0,
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

#### 9.买币我已付款

##### 9.1 方法原型

void otcBuyCoinPaid(String orderId, OnWalletListCallback callback);

**参数字段说明**

| 参数    | 类型   | 必传 | 描述   |
| ------- | ------ | ---- | ------ |
| orderId | string | 是   | 订单Id |

##### 9.2 返回结果

**示例：返回结果-正确时**

```java
{
	"code": 0,
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



### 6.OTC模块卖币

#### 1.卖币预下单

##### 1.1 方法原型

 void otcSellCoinAdvance(String tokenType,String payAmount,String recvAmount,String receiptAccount,String refundAddr,String payWay,String orderId ,OnWalletCallback callback);

**参数字段说明**

| 参数           | 类型   | 必传 | 描述                                                         |
| -------------- | ------ | ---- | ------------------------------------------------------------ |
| tokenType      | string | 是   | 需要卖出的币种类型                                           |
| payAmount      | string | 否   | 付款金额                                                     |
| recvAmount     | string | 否   | 付款币种数量(payAmount和recvAmount二选一,另一字段传nil或空串) |
| receiptAccount | string | 是   | 收款账号                                                     |
| refundAddr     | string | 是   | 卖币失败的时候币种的退款地址                                 |
| payWay         | string | 是   | 支付方式（AliPay，WechatPay，InternetBank，AlipayBankcard）  |
| orderId        | string | 是   | 卖币订单Id                                                   |

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

 void otcSellCoinConfirm(String orderId,OnWalletCallback callback);

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

 void otcSellCoinOrderDetails(String orderId ,OnWalletCallback callback );

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

void otcSellCoinOrderRecords(int page,int count,OnWalletCallback callback);

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

void otcSellCoinRate(String tokenType,OnWalletCallback callback);

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

void otcSellCoinImmediate(String tokenType,String payAmount,String recvAmount,String receiptAccount,String refundAddr,String payWay,OnWalletCallback callback);

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

 void otcSellCoinAssets（OnWalletCallback callback）;

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
            "tokenName": "USDX",
            "agentEnabled": false,
        },
        {
            "symbol":"USDX",
            "conAddr":"bcbMLpC7HFd8JCm6RXQiu1t7aX4GaiW5c4Cm",
            "decimals":"9",            
            "coinIcon":"http://test.6x.com/coin_icons/usdx.icon"
            "tokenName": "USDX",
            "agentEnabled": true,
            "agent":{
                "agentContract": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            	"agentFee": "0.01",
                "agentFeeToken": "USDX",
                "agentMethod": "Transfer(string,types.Address,bn.Number)",
            }    
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



### 7.USDT代收付款

#### 1.校验币种地址

##### 1.1 方法原型

void usdtVerifyAddress(String address,String tokenType,OnWalletCallback callback);

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

void usdtReceiptCoins(OnWalletListCallback callback);

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

void usdtReceiptAddress(String address,String tokenType,OnWalletCallback callback)

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

 void usdtPaymentCoins(OnWalletListCallback callback);

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

 void usdtPaymentAddress(String address,String tokenType,OnWalletListCallback callback);

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

#### 6.USDT代付转账

##### 6.1 方法原型

void usdtTransaction(String fromAddress,String password,bool broadcast,String toAddress,String toValue,String tokenType,String contract,String note, OnWalletCallback callback)

**参数字段说明**

| 字段名      | 类型   | 必须 | 说明                                   |
| ----------- | ------ | ---- | -------------------------------------- |
| fromAddress | String | 是   | 钱包地址                               |
| password    | String | 是   | 支付密码(开启免密支付时可传空串)       |
| broadcast   | bool   | 是   | 是否发送交易（true为钱包后台发送交易） |
| toAddress   | String | 是   | 代付款币种钱包地址                     |
| toValue     | String | 是   | 代付款币种数量                         |
| tokenType   | String | 是   | 代付款币种类型                         |
| contract    | String | 是   | 代付款币种合约地址                     |
| note        | String | 是   | 备注                                   |

##### 6.2 返回结果

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

#### 7. 获取USDT代收付款记录

##### 7.1 方法原型

void usdtPaymentRecords(String tokenType,String address,OnWalletCallback callback)

**参数字段说明**

| 参数      | 类型   | 必传 | 描述         |
| --------- | ------ | ---- | ------------ |
| tokenType | string | 否   | 代收付款币种 |
| address   | string | 否   | 用户的地址   |

##### 7.2 返回结果

**示例：返回结果-正确时**

```java
{
	"code": 0,
	"message": "ok",
    "data":{
        "info": {
			"page": 4,
			"totalpage": 401,
			"count": 50,
			"total": 20034
		},
		"list": [{
            "chainType": "BCB",
            "tokenType":"USDTERC",
            "tradeType": "pay", //pay,recv
            "addr": "bcbH8EnQ12jEeTXzPWKByVidjmaGXSTbHn3T",
            
            "from":"0xcade0735ff0adce2783f688d5183c41b72c1f03a",
            "to":"0xcade0735ff0adce2783f688d5183c41b72c1f03a",
            "memo":null, 
            "hash":"A87CECECDB59E7EC8...0513F68E2FF91592C",     
            "blockHeight": 123,
            "amount":"12.3",
            "fee":"0.3",
            "status":20, //交易中(20),已失败(40),已完成(100)
            "error":"资金校验失败，用户获得：0.145 DCT，交易限额：10 DCT",
            "createTime": "2020-06-29 12:00:00",
            "lastTime": "2020-06-29 12:00:00"
		}]
    }
}
```

**字段说明**

| 参数        | 类型    | 描述                                                         |
| ----------- | ------- | ------------------------------------------------------------ |
| chainType   | string  | 链类型                                                       |
| tokenType   | string  | 代收付款币种类型                                             |
| tradeType   | string  | 类型，pay：代付款，recv：代收款                              |
| addr        | string  | 用户地址                                                     |
| from        | string  | 转账地址，如果是代收款，则是用户的打款地址<br/>如果是代付款，则是用户付款的BCB地址 |
| to          | string  | 收款地址，如果是代收款，则是用户的BCB地址<br/>如果是代付款则是用户填的目标地址 |
| memo        | string  | 交易备注                                                     |
| hash        | string  | 交易hash，如果是代收款，则取bcb链上的hash<br />如果是代付款，取目标链的hash |
| blockHeight | int     | hash对应的区块高度                                           |
| amount      | decimal | 订单金额                                                     |
| fee         | decimal | 订单手续费                                                   |
| status      | int     | 订单状态//交易中(20),已失败(40),已完成(100)                  |
| error       | string  | 订单失败错误信息                                             |

**示例：返回结果-错误时**

```java
{
    "code":1008,
	"msg": "参数不能为空"
}
```

### 8.闪兑功能

#### 1.闪兑预下单

##### 1.1 方法原型

void exchangeAdvance(String tokenType, String payAmount, String recvTokenType, String recvAddr, String recvMemo, String refundAddr, String refundMemo, String orderId, OnWalletCallback callback);

**参数字段说明**

| 参数          | 类型   | 必传 | 描述                         |
| ------------- | ------ | ---- | ---------------------------- |
| tokenType     | string | 是   | 支付币种类型                 |
| payAmount     | string | 是   | 付款币种数量                 |
| recvTokenType | string | 是   | 接收的币种类型               |
| recvAddr      | string | 是   | 接收的币种地址               |
| recvMemo      | string | 否   | 接收地址标签                 |
| refundAddr    | string | 是   | 闪兑失败的时候币种的退款地址 |
| refundMemo    | string | 否   | 退款标签                     |
| orderId       | string | 是   | 闪兑订单Id                   |

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

| 字段名     | 类型    | 说明                   |
| ---------- | ------- | ---------------------- |
| expireTime | long    | 过期时间               |
| orderId    | string  | 订单Id                 |
| recvAmount | decimal | 获取数量               |
| payAmount  | decimal | 闪兑需要支付的币种数量 |
| rate       | decimal | 汇率                   |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 2.闪兑确认下单

##### 2.1 方法原型

void exchangeConfirm(String orderId, OnWalletCallback callback)

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



#### 3.查询闪兑订单详情

##### 3.1 方法原型

void exchangeOrderDetails(String orderId, OnWalletCallback callback)

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
        "payAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "payMemo": "",
        "recvTokenType": "BCB",
        "recvAmount": 10.0,
        "recvAddr": "",
        "recvMemo": "",
        "refundAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
        "refundMemo": "",
        "rate": 0,
        "fee": "",
        "status": 0, //创建(0),交易中(20),已取消(40),已完成(100)
        "remark": "",        
        "createTime": "2020-06-29 12:00:00",
        "lastTime": "2020-06-29 12:00:00"        
    }
}

```

**字段说明**

| 参数          | 类型    | 描述                                                    |
| ------------- | ------- | ------------------------------------------------------- |
| orderId       | string  | 订单编号                                                |
| tokenType     | string  | 支付币种                                                |
| payAmount     | decimal | 支付币种的数量                                          |
| payAddr       | string  | 支付目标地址                                            |
| payMemo       | string  | 支付地址标签                                            |
| recvTokenType | string  | 闪兑获得币种                                            |
| recvAmount    | decimal | 换的数量                                                |
| recvAddr      | string  | 收款地址                                                |
| recvMemo      | string  | 收款地址标签                                            |
| refundAddr    | string  | 退币的地址                                              |
| refundMemo    | string  | 退款地址标签                                            |
| rate          | decimal | 锁定汇率                                                |
| fee           | decimal | 用户总手续费                                            |
| status        | int     | 订单状态。<br>创建(0),交易中(20),已取消(40),已完成(100) |
| remark        | string  | 订单失败原因                                            |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 4.查询闪兑订单记录

##### 4.1 方法原型

void exchangeOrderRecords(int page, int count,  OnWalletCallback callback)

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
            "orderId": "IW01200204091426074b647c0aa",
            "tokenType": "DC",
            "payAmount": 10.0,
            "payAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            "payMemo": "",
            "recvTokenType": "BCB",
            "recvAmount": 10.0,
            "recvAddr": "",
            "recvMemo": "",
            "refundAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
            "refundMemo": "",
            "rate": 0,
            "fee": "",
            "status": 0, //创建(0),交易中(20),已取消(40),已完成(100)
            "expired": 1589971203987,
            "remark": "",        
            "createTime": "2020-06-29 12:00:00",
            "lastTime": "2020-06-29 12:00:00"
		}]
    }
}

```

##### 字段说明

| 字段          | 类型    | 描述                                                    |
| ------------- | ------- | ------------------------------------------------------- |
| orderId       | string  | 订单编号                                                |
| tokenType     | string  | 支付币种                                                |
| payAmount     | decimal | 支付币种的数量                                          |
| payAddr       | string  | 支付目标地址                                            |
| payMemo       | string  | 支付地址标签                                            |
| recvTokenType | string  | 闪兑获得币种                                            |
| recvAmount    | decimal | 换的数量                                                |
| recvAddr      | string  | 收款地址                                                |
| recvMemo      | string  | 收款地址标签                                            |
| refundAddr    | string  | 退币的地址                                              |
| refundMemo    | string  | 退款地址标签                                            |
| rate          | decimal | 锁定汇率                                                |
| fee           | decimal | 用户总手续费                                            |
| status        | int     | 订单状态。<br>创建(0),交易中(20),已取消(40),已完成(100) |
| expired       | long    | 过期时间                                                |
| remark        | string  | 订单失败原因                                            |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 5.查询闪兑汇率

##### 5.1 方法原型

 void queryExchangeRate( OnWalletCallback callback)

**参数字段说明**

无

##### 5.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "rates":{
            "BTC":{                    // payCoin
            	"accuracy":4,
                "channel":{            // 闪兑通道
                	"ETH":{         // 通道类型gotCoin
                        "accuracy":4,
                        "min":0.1,    // 最小下单量，以此payCoin为单位
                        "max":11000,    // 最大下单量，以此payCoin为单位
                        "rate": 0.021  // 1 payCoin = rate gotCoin
                    },
                    "BCB":{
                        "accuracy":4,
                        "min":0.09,
                        "max":19000,
                        "rate": 0.021
                    },
                    "DC":{
                        "accuracy":4,
                        "min":0.08,
                        "max":18000,
                        "rate": 0.021
                    },
                    "USDT":{
                        "accuracy":4,
                        "min":0.02,
                        "max":20000,
                        "rate": 0.021
                    }
                }
            }            
		}
    }
}

```

**字段说明**

| 参数     | 类型    | 描述                   |
| -------- | ------- | ---------------------- |
| accuracy | int     | 支持闪兑支付币种的精度 |
| channel  | map     | 每个闪兑通道的限额     |
| accuracy | int     | 获得币种的精度         |
| min      | decimal | 最小闪兑数量           |
| max      | decimal | 最大闪兑数量           |
| rate     | decimal | 汇率                   |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



#### 6.一步式闪兑下单

##### 6.1 方法原型

void exchangeImmediate(String tokenType, String payAmount, String recvTokenType, String recvAddr, String recvMemo, String refundAddr, String refundMemo, String orderId, OnWalletCallback callback);

**参数字段说明**

**参数字段说明**

| 参数          | 类型   | 必传 | 描述                         |
| ------------- | ------ | ---- | ---------------------------- |
| tokenType     | string | 是   | 支付币种类型                 |
| payAmount     | string | 是   | 付款币种数量                 |
| recvTokenType | string | 是   | 接收的币种类型               |
| recvAddr      | string | 是   | 接收的币种地址               |
| recvMemo      | string | 否   | 接收地址标签                 |
| refundAddr    | string | 是   | 闪兑失败的时候币种的退款地址 |
| refundMemo    | string | 否   | 退款标签                     |

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

#### 7.反向查询闪兑汇率

##### 5.1 方法原型

 void reverseQueryExchangeRate( OnWalletCallback callback)

**参数字段说明**

无

##### 5.2 返回结果

**示例：返回结果-正确时**

```java
{
    "code":0,
	"msg": "ok",
    "result":{
        "rates":{
            "BTC":{                    // payCoin
            	"accuracy":4,
                "channel":{            // 闪兑通道
                	"ETH":{         // 通道类型gotCoin
                        "accuracy":4,
                        "min":0.1,    // 最小下单量，以此payCoin为单位
                        "max":11000,    // 最大下单量，以此payCoin为单位
                        "rate": 0.021  // 1 payCoin = rate gotCoin
                    },
                    "BCB":{
                        "accuracy":4,
                        "min":0.09,
                        "max":19000,
                        "rate": 0.021
                    },
                    "DC":{
                        "accuracy":4,
                        "min":0.08,
                        "max":18000,
                        "rate": 0.021
                    },
                    "USDT":{
                        "accuracy":4,
                        "min":0.02,
                        "max":20000,
                        "rate": 0.021
                    }
                }
            }            
		}
    }
}

```

**字段说明**

| 参数     | 类型    | 描述                   |
| -------- | ------- | ---------------------- |
| accuracy | int     | 支持闪兑支付币种的精度 |
| channel  | map     | 每个闪兑通道的限额     |
| accuracy | int     | 获得币种的精度         |
| min      | decimal | 最小闪兑数量           |
| max      | decimal | 最大闪兑数量           |
| rate     | decimal | 汇率                   |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```



### 9.其他接口

#### 1.获取服务器时间

##### 1.1 方法原型

void getServiceTimestamp( OnWalletCallback callback);

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

#### 2  获取隐私声明

##### 2.1 方法原型

void getPrivacyAndAgreement(OnWalletCallback callback);

**参数字段说明**

无

##### 2.2 返回结果

**返回结果-正确时**

```java
{
	"code": 0,
	"message": "ok",
    "data":{
        "privacy":"",
        "agreement": ""
    }
}

```

**字段说明**

| 参数      | 类型   | 描述     |
| --------- | ------ | -------- |
| privacy   | string | 隐私声明 |
| agreement | string | 用户协议 |

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "其他错误"
}
```

#### 3  获取App最新版本

##### 2.1 方法原型

void getVersion(String platform,OnWalletCallback callback);

**请求消息params参数说明**

| 参数     | 类型   | 必传 | 描述                |
| -------- | ------ | ---- | ------------------- |
| platform | string | 否   | 平台（ios/android） |

**返回结果-正确时**

```java
{
    "code": 0,
    "message": "ok",
    "data":{
        "ios": {
            "url": "",
            "version":"1.0.1",
            "force": false,
            "msg": "123"
        },
        "android": {
            "url": "",
            "version":"1.0.1",
            "force": false,
            "msg": "123"
        }
    }
}


```

**字段说明**

| 参数      | 类型   | 描述     |
| --------- | ------ | -------- |
| privacy   | string | 隐私声明 |
| agreement | string | 用户协议 |

**返回结果-错误时**

```java
{
    "code":-1,
	"msg": "其他错误"
}
```

### II 附录

#### 13.1 OnWalletCallback

```
interface OnWalletCallback<T> {

    void onSuccess(T result); //T 为异步回调的返回结果

    void onFail(int errorCode,String message);//errorCode错误码，message错误信息

}
```

#### 13.2 OnWalletListCallback

```
interface OnWalletListCallback<T> {

    void onSuccess(List<T> resultList);//T 为异步回调的返回结果

    void onFail(int errorCode,String message);

}
```

#### 13.3统一状态码

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



