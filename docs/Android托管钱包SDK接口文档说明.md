## **Android托管钱包SDK接口文档说明**





### 版本&更新记录

| 版本号  | 作者 | 日期       | 更新内容                                                     |
| ------- | ---- | ---------- | ------------------------------------------------------------ |
| v.1.0.0 | jjm  | 2020-06-16 | 初始版本                                                     |
| v.1.0.1 | jjm  | 2020-06-28 | 新增OTC买币回调和设置网络请求超时时间回调                    |
| v.1.0.2 | jjm  | 2020-06-29 | 调整5-3/5-4加了俩个字段，添加一步式直接买币，SDK内部处理订单ID，去除5-4订单ID参数 |

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

boolean setTimeout(String timeout);

 **输入参数说明**

| 参数名  | 类型   | 必须 | 说明                 |
| ------- | ------ | ---- | -------------------- |
| timeout | String | 是   | 超时时间（单位：秒） |

##### 3.2 返回结果

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

**void getCoinTransactionDetail(String address,String contract, int page,int count,OnWalletListCallback callback);**

**参数字段说明**

| 字段名     | 类型                 | 必须 | 说明                                                 |
| ---------- | -------------------- | ---- | ---------------------------------------------------- |
| walletAddr | string               | 是   | 钱包地址                                             |
| contract   | string               | 是   | 币种合约地址,(传null表示当前用户所有币种查询)        |
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

void cloudWalletTransation(String walletAddr, String password，String broadcast, String walletCall, OnWalletCallback callback);

**参数字段说明**

| 字段名     | 类型             | 必须 | 说明                                                         |
| ---------- | ---------------- | ---- | ------------------------------------------------------------ |
| walletAddr | String           | 是   | 钱包地址                                                     |
| password   | String           | 是   | 支付密码                                                     |
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



### II 附录

##### 13.1 OnWalletCallback

```
interface OnWalletCallback<T> {

    void onSuccess(T result); //T 为异步回调的返回结果

    void onFail(int errorCode,String message);//errorCode错误码，message错误信息

}
```

##### 13.2 OnWalletListCallback

```
interface OnWalletListCallback<T> {

    void onSuccess(List<T> resultList);//T 为异步回调的返回结果

    void onFail(int errorCode,String message);

}
```

#### 13.3统一状态码

| code | 描述                |
| ---- | ------------------- |
| 0    | 成功                |
| 1001 | 无效token           |
| 1002 | 无效时间戳          |
| 1003 | 无效链类型          |
| 1004 | 无效appId           |
| 1005 | 无效商户            |
| 1006 | appId和apiKey不匹配 |
| 1007 | 验证码不正确        |
| 1008 | 参数不能为空        |
| 1009 | 账户已被绑定        |
| 1010 | 格式不正确          |
| 1011 | 无效地址            |
| 1012 | 参数过长,不能超过   |
| 1013 | 免密支付已过期      |
| -1   | 位置错误。          |



### 4.免密支付

#### 1.请求免密支付授权

##### 1.1 方法原型

void setSecretFreePayment(String password,String time,OnWalletListCallback  callback);

**参数字段说明**

| 字段名   | 类型             | 必须 | 说明                                                         |
| -------- | ---------------- | ---- | ------------------------------------------------------------ |
| password | string           | 是   | 支付密码，MD5(ikey.cloud: + password)                        |
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

### 5.OTC模块

#### 1.买币预下单

##### 1.1 方法原型

 void otcBuyCoinAdvance(String tokenType,decimal payAmount,decimal recvAmount,String recvAddr,String payWay,String orderId ,OnWalletCallback callback);

**参数字段说明**

| 参数       | 类型             | 必传 | 描述                                                 |
| ---------- | ---------------- | ---- | ---------------------------------------------------- |
| tokenType  | string           | 是   | 需要购买的币种类型                                   |
| payAmount  | decimal          | 否   | 付款金额                                             |
| recvAmount | decimal          | 否   | 获取币种数量(payAmount和recvAmount二选一)            |
| recvAddr   | string           | 是   | 接收币种的地址                                       |
| payWay     | string           | 是   | 支付方式（AliPay，WechatPay）                        |
| orderId    | string           | 是   | 订单Id ，Iw年月日时分秒0-9和a-z6位随机数             |
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
    "code":0,
	"msg": "ok",
    "result":{
        "rates":{
            "BTC":{                    // gotCoin
            	"AliPay":0.021,        // payWay : rate
            	"WechatPay":0.022,     // 1 CNY = rate gotCoin
            	"InternetBank":0.020,
            	"accuracy":4,
                "min":0.1,
                "max":10000
            },
            "ETH":{
            	"AliPay":0.00125,        
            	"WechatPay":0.00126,     
            	"InternetBank":0.00124,  
            	"accuracy":4,
                "min":0.1,
                "max":10000
            }
		}
    }
}

```

**字段说明**

| 参数         | 类型    | 描述                                         |
| ------------ | ------- | -------------------------------------------- |
| AliPay       | decimal | 使用支付宝的汇率（1CNY能购买币种的数量）     |
| WechatPay    | decimal | 使用微信支付的汇率（1CNY能购买币种的数量）   |
| InternetBank | decimal | 使用银行卡支付的汇率（1CNY能购买币种的数量） |
| accuracy     | int     | 支持购买币种的精度                           |
| min          | decimal | 币种最小购买数量                             |
| max          | decimal | 币种最大购买数量                             |

**示例：返回结果-错误时**

```java
{
    "code":1001,
	"msg": "无效token"
}
```

#### 6.一步式直接买币下单

##### 6.1 方法原型

 void otcBuyCoinImmediate(String tokenType,decimal payAmount,decimal recvAmount,String recvAddr,String payWay,OnWalletCallback callback);，、

**参数字段说明**

| 参数       | 类型   | 必传 | 描述                                                         |
| ---------- | ------ | ---- | ------------------------------------------------------------ |
| tokenType  | string | 是   | 需要购买的币种类型（当前支持币种：BCB、DC）                  |
| payAmount  | string | 否   | 付款金额                                                     |
| recvAmount | string | 否   | 获取币种数量(payAmount和recvAmount二选一,另一字段传nil或空串) |
| recvAddr   | string | 是   | 收款地址                                                     |
| payWay     | string | 是   | 支付方式（AliPay，WechatPay）                                |

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





