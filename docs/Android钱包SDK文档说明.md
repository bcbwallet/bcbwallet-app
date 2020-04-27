# Android钱包SDK文档说明

## 版本&更新记录

| 版本号  | 作者      | 日期       | 更新内容                |
| ------- | --------- | ---------- | ----------------------- |
| v.1.0.0 | bcbwallet | 2019-04-01 | 初始版本                |
| v2.0    | bcbwalelt | 2019-06-25 | 2.0链接口               |
| v3.0    | bcbwallet | 2019-11-14 | 增加2.13-2.15侧链的支持 |
| v4.0    | bcbwallet | 2019-12-04 | 增加域名切换            |
| v5.0    | bcbwallet | 2020-04-27 | 增加托管钱包模块        |

## 功能说明

本文档提供钱包的SDK访问接口说明。Android版本。

## 接口访问方式

普通方法调用的方式，以下接口都是WalletAssistant的静态方法

## 1.初始化

### 1.1 初始化接口

方法原型：

boolean init(Context context,String appId);

方法原型：

| 参数名  | 类型    | 必须 | 说明                 |
| ------- | ------- | ---- | -------------------- |
| context | Context | 是   | Application的Context |
| appId   | String  | 是   | 分配的appid          |

返回结果:

true：初始化成功，false：初始化失败

方法说明：

全局的初始化接口，建议在Application的onCreate中调用

### 1.2 设置接入方自生成的ID

方法原型：

void setPushId(String pushId);

参数说明：

| 字段名 | 类型   | 必须 | 说明                       |
| ------ | ------ | ---- | -------------------------- |
| pushId | string | 是   | 接入方自生成的ID（可为空） |

### 1.3 获取当前环境所有的链的信息

方法原型：

void getChainInfo(final OnWalletCallback<List<String>> callback);

参数说明：

| 字段名   | 类型                           | 必须 | 说明                                                         |
| -------- | ------------------------------ | ---- | ------------------------------------------------------------ |
| callback | OnWalletCallback<List<String>> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback),成功返回所有的链的名称 |

返回结果：

无

调用时机：

一般情况是需要在需要切换链之前进行调用获取链的信息，然后选取一个链

示例

```java
WalletAssistant.getChainInfo(new OnWalletCallback<List<String>>() {    
    @Override    
    public void onSuccess(List<String> result) {
        //TODO result = ["devtest","jiujiu"];
	}    
    @Override    
    public void onFail(int errorCode, String message) {
    }
});
```

### 1.4 切换链

方法原型

void switchChain(String chainName,final OnWalletCallback<String> callback)；

参数说明：

| 字段名    | 类型                     | 必须 | 说明                                                         |
| --------- | ------------------------ | ---- | ------------------------------------------------------------ |
| chainName | String                   | 是   | 切换到的链的名称，例如devtest,jiujiu                         |
| callback  | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback),成功透传chainName |

调用时机：

1.3方法拿到所有的链的列表以后选择其中的一个进行切换

### 1.5 获取当前的链的名称

方法原型

String getCurrentChain();

参数说明：

略

返回结果：

String  当前使用的链的名称，例如 devtest,jiujiu

### 1.6 获取域名列表

方法原型：

void getDomainList(final OnWalletCallback<List<String>> callback);

参数说明：

| 字段名   | 类型                           | 必须 | 说明                                                         |
| -------- | ------------------------------ | ---- | ------------------------------------------------------------ |
| callback | OnWalletCallback<List<String>> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback),成功返回所有的链的名称 |

返回结果：

无

调用时机：

一般情况是需要在需要切换域名之前进行调用获取可用域名，然后选取一个重设域名

示例

```java
WalletAssistant.getDomainList(new OnWalletCallback<List<String>>() {    
    @Override    
    public void onSuccess(List<String> result) {
        //TODO result = ["https://wallet.bcbchain.io","https://wallet2.bcbchain.io"];
	}    
    @Override    
    public void onFail(int errorCode, String message) {
    }
});
```

### 1.7 设置域名

方法原型

void setWalletDomain(String domain,final OnWalletCallback<String> callback)；

参数说明：

| 字段名   | 类型                     | 必须 | 说明                                                         |
| -------- | ------------------------ | ---- | ------------------------------------------------------------ |
| domain   | String                   | 是   | 域名地址，例如"https://wallet2.bcbchain.io"                  |
| callback | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback),成功透传chainName |

调用时机：

1.6方法拿到所有的域名列表以后选择其中的一个进行设置

## 2.钱包管理

### 2.1 创建钱包

方法原型：

**void createWallet(String name,String password,String recommend,OnWalletCallback<CreateWalletEntity> onWalletCallback);**

参数说明：

| 参数名           | 类型                                 | 必须 | 说明                                                         |
| ---------------- | ------------------------------------ | ---- | ------------------------------------------------------------ |
| name             | String                               | 是   | 钱包名称                                                     |
| password         | String                               | 是   | 钱包密码                                                     |
| recommend        | String                               | 否   | 推荐人的钱包地址                                             |
| onWalletCallback | OnWalletCallback<CreateWalletEntity> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback),CreateWalletEntity见附录[7.3](#7.3 CreateWalletEntity) |

返回结果:

无

### 2.2 获取所有钱包

方法原型：

void OnWalletListCallback<WalletEntity> getWallets();

参数说明：

| 参数名   | 类型                               | 必须 | 说明                                             |
| -------- | ---------------------------------- | ---- | ------------------------------------------------ |
| callback | OnWalletListCallback<WalletEntity> | 是   | 回调接口，见附录[7.2](#7.2 OnWalletListCallback) |

返回结果：

无

### 2.3 导出助记词

方法原型：

**void exportMnemonicWords(String address,String password,OnWalletCallback<String> callback);**

参数说明：

| 参数名   | 类型                     | 必须 | 说明                                         |
| -------- | ------------------------ | ---- | -------------------------------------------- |
| address  | String                   | 是   | 钱包地址                                     |
| password | String                   | 是   | 钱包密码                                     |
| callback | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback) |

返回结果:

无

### 2.4 导出私钥

方法原型：

**void exportPrivateKey(String address,String password,OnWalletCallback<String> callback);**

参数说明：

| 参数名   | 类型                     | 必须 | 说明                                         |
| -------- | ------------------------ | ---- | -------------------------------------------- |
| address  | String                   | 是   | 钱包地址                                     |
| password | String                   | 是   | 钱包密码                                     |
| callback | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback) |

返回结果:

无

### 2.5 导出keystore

方法原型：

**void exportKeystore(String address,String password,OnWalletCallback<String> callback);**

参数说明：

| 参数名   | 类型                     | 必须 | 说明                                         |
| -------- | ------------------------ | ---- | -------------------------------------------- |
| address  | String                   | 是   | 钱包地址                                     |
| password | String                   | 是   | 钱包密码                                     |
| callback | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback) |

返回结果:

无

### 2.6 导入私钥生成钱包

方法原型：

**void importPrivateKey(String name,String privatekey,String password,String recommend,OnWalletCallback<WalletEntity> callback);**

参数说明：

| 字段名     | 类型                           | 必须 | 说明                                                         |
| ---------- | ------------------------------ | ---- | ------------------------------------------------------------ |
| name       | String                         | 是   | 钱包名称                                                     |
| privatekey | String                         | 是   | 私钥                                                         |
| password   | String                         | 是   | 钱包密码                                                     |
| recommend  | String                         | 否   | 推荐人的钱包地址                                             |
| callback   | OnWalletCallback<WalletEntity> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，WalletEntity参见[7.4](#7.4 WalletEntity) |

返回结果:

无

### 2.7 导入keystore生成钱包

方法原型：

**void importKeystore(String name,String keystore,String password,String recommend,OnWalletCallback<WalletEntity> callback);**

参数说明：

| 字段名     | 类型                           | 必须 | 说明                                                         |
| ---------- | ------------------------------ | ---- | ------------------------------------------------------------ |
| name       | String                         | 是   | 钱包名称                                                     |
| privatekey | String                         | 是   | 私钥                                                         |
| password   | String                         | 是   | 钱包密码                                                     |
| recommend  | String                         | 否   | 推荐人的钱包地址                                             |
| callback   | OnWalletCallback<WalletEntity> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，WalletEntity参见[7.4](#7.4 WalletEntity) |

返回结果:

无

### 2.8 导入助记词生成钱包

方法原型：

**void importMnemonicWords(String name,String mnenonicwords,String password,String recommend,OnWalletCallback<WalletEntity> callback);**

参数说明：

| 字段名     | 类型                           | 必须 | 说明                                                         |
| ---------- | ------------------------------ | ---- | ------------------------------------------------------------ |
| name       | String                         | 是   | 钱包名称                                                     |
| privatekey | String                         | 是   | 私钥                                                         |
| password   | String                         | 是   | 钱包密码                                                     |
| recommend  | String                         | 否   | 推荐人的钱包地址                                             |
| callback   | OnWalletCallback<WalletEntity> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，WalletEntity参见[7.4](#7.4 WalletEntity) |

返回结果:

无

### 2.9 验证钱包密码

方法原型：

**void verifyPassword(String address,String password,OnWalletCallback<Boolean> callback);**

参数说明：

| 字段名   | 类型                           | 必须 | 说明                                                         |
| -------- | ------------------------------ | ---- | ------------------------------------------------------------ |
| address  | String                         | 是   | 钱包地址                                                     |
| password | String                         | 是   | 钱包密码                                                     |
| callback | OnWalletCallback<WalletEntity> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，WalletEntity参见[7.4](#7.4 WalletEntity) |

返回结果:

无

### 2.10 修改钱包密码

方法原型：

**void changePassword(String address,String oldPassword,String newPassword,OnWalletCallback<Boolean> callback);**

参数说明：

| 字段名      | 类型                      | 必须 | 说明                                                         |
| ----------- | ------------------------- | ---- | ------------------------------------------------------------ |
| address     | String                    | 是   | 钱包地址                                                     |
| oldPassword | String                    | 是   | 钱包旧密码                                                   |
| newPassword | String                    | 是   | 钱包新密码，必须是至少8位的字母数字组合                      |
| callback    | OnWalletCallback<Boolean> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback),true 成功，false 失败 |

返回结果:

无

### 2.11 修改钱包名称

方法原型：

void changeWalletName(String address,String newName,OnWalletCallback<Boolean> callback);**

参数说明：

| 字段名   | 类型                      | 必须 | 说明                                                         |
| -------- | ------------------------- | ---- | ------------------------------------------------------------ |
| address  | String                    | 是   | 钱包地址                                                     |
| newName  | String                    | 是   | 新钱包名称                                                   |
| callback | OnWalletCallback<Boolean> | 是   | 回调接口，见附录[7.1](#7.1%20OnWalletCallback)，true 成功，false 失败 |

返回结果:

无

### 2.12 删除钱包

方法原型：

void deleteWallet(String address,String password,OnWalletCallback<Boolean> callback);**

参数说明：

| 字段名   | 类型                      | 必须 | 说明                                                         |
| -------- | ------------------------- | ---- | ------------------------------------------------------------ |
| address  | String                    | 是   | 钱包地址                                                     |
| password | String                    | 是   | 钱包密码                                                     |
| callback | OnWalletCallback<Boolean> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback),true 成功，false 失败 |

返回结果:

无

## 3 资产管理

### 3.1 钱包转账

方法原型：

**void walletTransaction(String address,String password,String coinAddr,String toAddr,String value,String note,OnWalletCallback<String> callback);**

参数说明：

| 字段名   | 类型                     | 必须 | 说明                                                         |
| -------- | ------------------------ | ---- | ------------------------------------------------------------ |
| address  | String                   | 是   | 钱包地址                                                     |
| password | String                   | 是   | 钱包密码                                                     |
| coinAddr | String                   | 是   | 要转账币种的合约地址                                         |
| toAddr   | String                   | 是   | 转账到的目标地址                                             |
| value    | String                   | 是   | 转账的金额，例如"102.23"                                     |
| note     | String                   | 否   | 转账的备注，对于BCB链，这个字段最终会写入到区块中            |
| callback | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，String为txHash |

返回结果:

无

### 3.2 通用支付-通用型合约支付接口

方法原型：

**void walletCommonPay(String address,String password,String walletCall,OnWalletCallback<String> callback);**

参数说明：

| 字段名     | 类型                     | 必须 | 说明                                                         |
| ---------- | ------------------------ | ---- | ------------------------------------------------------------ |
| version    | int                      | 是   | 1：1.0支付    2：2.0支付    3：3.0支付                       |
| address    | String                   | 是   | 钱包地址                                                     |
| password   | String                   | 是   | 钱包密码                                                     |
| walletCall | String                   | 是   | json串，此字段根据不同的合约定义有不同的数据格式；具体请参见《BCB钱包通用支付接入规范》总描述 |
| callback   | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，String为txHash |

返回结果:

无

**示例1.0链：展开后的格式**

```java
 {
		"conAddr": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
		"methodName": "Transfer",
		"methodParam": [{
				"name": "receiver",
				"type": "smc.Address",
				"value": "bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9"
			},
			{
				"name": "_bcb",
				"type": "big.Int-decimal",
				"value": "0.01"
			}
		],
		"methodRet": "smc.Error"
	}
```

**示例2.0链：展开后的格式**

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

**示例3.0链：展开后的格式**

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

### 3.3 查询指定地址资产

方法原型：

**void getAddrBalance(String address,String legalSymbol,OnWalletListCallback<BalanceEntity> callback);**

参数说明：

| 字段名      | 类型                                | 必须 | 说明                                                         |
| ----------- | ----------------------------------- | ---- | ------------------------------------------------------------ |
| address     | String                              | 是   | 钱包地址                                                     |
| legalSymbol | String                              | 是   | 资产的法币计价单位，人民币为：CNY；美元为：USD               |
| callback    | OnWalletListCallback<BalanceEntity> | 是   | 回调接口，见附录[7.2](#7.2 OnWalletListCallback)，BalanceEntity见[7.5](#7.5 BalanceEntity) |

返回结果:

无

### 3.4 获取系统可添加资产列表

方法原型：

**void getAssets(String address,OnWalletListCallback<AssetEntity> callback);**

参数说明：

| 字段名   | 类型                              | 必须 | 说明                                                         |
| -------- | --------------------------------- | ---- | ------------------------------------------------------------ |
| address  | String                            | 是   | 钱包地址                                                     |
| callback | OnWalletListCallback<AssetEntity> | 是   | 回调接口，见附录[7.2](#7.2 OnWalletListCallback)，AssetEntity见[7.6](#7.6 AssetEntity) |

返回结果:

无

### 3.5 查询指定地址、指定币种信息

方法原型：

**void getCoinDetail(String address,String coinAddr,String legalSymbol,OnWalletCallback<AssetDetailEntity> callback);**

参数说明：

| 字段名      | 类型                                | 必须 | 说明                                                         |
| ----------- | ----------------------------------- | ---- | ------------------------------------------------------------ |
| address     | String                              | 是   | 钱包地址                                                     |
| conAddr     | String                              | 是   | 币种合约地址                                                 |
| legalSymbol | String                              | 是   | 币种资产的法币计价单位，人民币为：CNY；美元为：USD           |
| callback    | OnWalletCallback<AssetDetailEntity> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，AssetDetailEntity见[7.7](#7.7 AssetDetailEntity) |

返回结果:

无

### 3.6 查询指定币种交易记录

方法原型：

**void getCoinTransactionDetail(String address,String coinAddr,int page,int count,OnWalletListCallback<TransactionRecord> callback);**

参数说明：

| 字段名     | 类型                                    | 必须 | 说明                                                         |
| ---------- | --------------------------------------- | ---- | ------------------------------------------------------------ |
| walletAddr | string                                  | 是   | 钱包地址                                                     |
| conAddr    | string                                  | 是   | 币种合约地址                                                 |
| page       | int                                     | 是   | 页码从0开始                                                  |
| count      | int                                     | 是   | 条数                                                         |
| callback   | OnWalletListCallback<TransactionRecord> | 是   | 回调接口，见附录[7.2](#7.2 OnWalletListCallback)，TransactionRecord见[7.8](#7.8 TransactionRecord) |

返回结果:

无

## 4.OTC及闪兑模块

普通方法调用的方式，以下接口都是OtcFastAssistance的静态方法

### 4.1 初始化

方法原型：

void init();

参数说明：

略

方法说明：

OTC模块初始化接口，建议在Application的onCreate中调用

### 4.2 OTC开发环境设置

方法原型：

void setMode(int mode);

参数说明：

| 字段名 | 类型 | 必须 | 说明                     |
| ------ | ---- | ---- | ------------------------ |
| mode   | int  | 是   | 0：测试环境、1：正式环境 |

### 4.3 OTC模块皮肤主题设置

方法原型：

void setOtcTheme(int otcTheme);

参数说明：

| 字段名   | 类型 | 必须 | 说明                     |
| -------- | ---- | ---- | ------------------------ |
| otcTheme | int  | 是   | 0：白色主题、1：暗色主题 |

### 4.4 OTC买币强制绑定银行卡设置

方法原型：

void setOtcBuyBindBankCard(boolean bindCard);

参数说明：

| 字段名   | 类型    | 必须 | 说明                      |
| -------- | ------- | ---- | ------------------------- |
| bindCard | boolean | 是   | 默认不强制，强制绑定为YES |

### 4.5 OTC入口

方法原型：

void gotoOtc();

参数说明：

略

### 4.6 闪兑入口

方法原型：

void gotoFastChange();

参数说明：

略

## 5 工具

普通方法调用的方式，以下接口都是WalletAssistant的静态方法

### 5.1 加密

方法原型：

void encryptContent(String content,OnWalletCallback<String> callback);

参数说明：

| 字段名   | 类型                     | 必须 | 说明                                                         |
| -------- | ------------------------ | ---- | ------------------------------------------------------------ |
| content  | String                   | 是   | 加密内容                                                     |
| callback | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，String为加密后内容 |

### 5.2 解密

方法原型：

void decryptContent(String encContent,OnWalletCallback<String> callback);

参数说明：

| 字段名   | 类型                     | 必须 | 说明                                                         |
| -------- | ------------------------ | ---- | ------------------------------------------------------------ |
| content  | String                   | 是   | 解密内容                                                     |
| callback | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，String为解密后内容 |

### 5.3 生成密钥对

方法原型：

void genKeyPair(final OnWalletCallback<KeyPairEntity> callback);

参数说明：

| 字段名   | 类型                            | 必须 | 说明                                                         |
| -------- | ------------------------------- | ---- | ------------------------------------------------------------ |
| callback | OnWalletCallback<KeyPairEntity> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，回调接口，KeyPairEntity见[7.10](#7.10 KeyPairEntity) |

### 5.4 私钥签名

方法原型：

void genSign(String privateKey, String hexData, final OnWalletCallback<SignResultEntity> callback);

参数说明：

| 字段名     | 类型                               | 必须 | 说明                                                         |
| ---------- | ---------------------------------- | ---- | ------------------------------------------------------------ |
| privateKey | String                             | 是   | 私钥hex                                                      |
| hexData    | String                             | 是   | 待签名内容hex                                                |
| callback   | OnWalletCallback<SignResultEntity> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，SignResultEntity见[7.11](#7.11 SignResultEntity) |

### 5.5 数据验签

方法原型：

void verifyClientData(String content, String pubKey, String signature, OnWalletCallback<Boolean> callback);

参数说明：

| 字段名    | 类型                      | 必须 | 说明                                                         |
| --------- | ------------------------- | ---- | ------------------------------------------------------------ |
| content   | String                    | 是   | 待验签内容hex                                                |
| pubKey    | String                    | 是   | 验签公钥hex                                                  |
| signature | String                    | 是   | 签名hex                                                      |
| callback  | OnWalletCallback<Boolean> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，true 成功，false 失败 |

### 5.6 根据助记词返回对应钱包地址

方法原型：

void getAddrFromMnenonicWords(final String mnenonicwords,OnWalletCallback<String> callback);

参数说明：

| 字段名        | 类型                     | 必须 | 说明                                                         |
| ------------- | ------------------------ | ---- | ------------------------------------------------------------ |
| mnenonicwords | String                   | 是   | 助记词                                                       |
| callback      | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，String为钱包地址 |

### 5.7 根据私钥返回对应钱包地址

方法原型：

void getAddrFromPrivateKey(final String privatekey,OnWalletCallback<String> callback);

参数说明：

| 字段名     | 类型                     | 必须 | 说明                                                         |
| ---------- | ------------------------ | ---- | ------------------------------------------------------------ |
| privatekey | String                   | 是   | 私钥                                                         |
| callback   | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，String为钱包地址 |

### 5.8 根据Keystore返回对应钱包地址

方法原型：

void getAddrFromKeyStore(final String keystore, final String password, OnWalletCallback<String> callback);

参数说明：

| 字段名   | 类型                     | 必须 | 说明                                                         |
| -------- | ------------------------ | ---- | ------------------------------------------------------------ |
| keystore | String                   | 是   | keystore                                                     |
| password | String                   | 是   | 密码                                                         |
| callback | OnWalletCallback<String> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，String为钱包地址 |

## 6.托管钱包模块

### 6.1 设置域名

方法原型：

boolean setCloudDomain(String domain);

参数说明：

| 参数名 | 类型   | 必须 | 说明                                            |
| ------ | ------ | ---- | ----------------------------------------------- |
| domain | String | 是   | 域名（例：https://api.iwallet.cloud/pkey_api/） |

返回结果:

true：设置成功，false：设置失败

### 6.2 设置商户信息

方法原型：

boolean setMerchantId(String merchantId, String remoteDHPubKey);

参数说明：

| 参数名         | 类型   | 必须 | 说明         |
| -------------- | ------ | ---- | ------------ |
| merchantId     | String | 是   | 商户ID       |
| remoteDHPubKey | String | 是   | 商户对应公钥 |

返回结果:

true：设置成功，false：设置失败

### 6.3 获取验证码

方法原型：void getCode(String account, OnWalletCallback<Boolean> callback);

参数说明：

| 字段名   | 类型                      | 必须 | 说明                                                         |
| -------- | ------------------------- | ---- | ------------------------------------------------------------ |
| account  | String                    | 是   | 手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |
| callback | OnWalletCallback<Boolean> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，true 成功，false 失败 |

### 6.4 绑定账号

方法原型：void bindAccount(String account, String code, OnWalletCallback<Boolean> callback);

参数说明：

| 字段名   | 类型                      | 必须 | 说明                                                         |
| -------- | ------------------------- | ---- | ------------------------------------------------------------ |
| account  | String                    | 是   | 手机号(加国际区号，例：+86139********)或邮箱（例：12345@qq.com） |
| code     | String                    | 是   | 验证码                                                       |
| callback | OnWalletCallback<Boolean> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，true 成功，false 失败 |

### 6.5 数据签名

方法原型：

void secretSign(String content, final OnWalletCallback<SignResultEntity> callback);

参数说明：

| 字段名   | 类型                               | 必须 | 说明                                                         |
| -------- | ---------------------------------- | ---- | ------------------------------------------------------------ |
| content  | String                             | 是   | 待签名内容hex                                                |
| callback | OnWalletCallback<SignResultEntity> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，SignResultEntity见[7.11](#7.11 SignResultEntity) |

### 6.6 数据验签

方法原型：

void verifySign(String content, String signature,OnWalletCallback<Boolean> callback);

参数说明：

| 字段名    | 类型                      | 必须 | 说明                                                         |
| --------- | ------------------------- | ---- | ------------------------------------------------------------ |
| content   | String                    | 是   | 待验签内容hex                                                |
| signature | String                    | 是   | 签名hex                                                      |
| callback  | OnWalletCallback<Boolean> | 是   | 回调接口，见附录[7.1](#7.1 OnWalletCallback)，true 成功，false 失败 |

## 7 附录

### 7.1 OnWalletCallback

```java
interface OnWalletCallback<T> {

	void onSuccess(T result); //T 为异步回调的返回结果

	void onFail(int errorCode,String message);//errorCode错误码，message错误信息

}
```

### 7.2 OnWalletListCallback

```java
interface OnWalletListCallback<T> {

	void onSuccess(List<T> resultList);//T 为异步回调的返回结果

	void onFail(int errorCode,String message);

}
```

### 7.3 CreateWalletEntity

```java
class CreateWalletEntity {
	private String name;//钱包名称
    private String mnemonicWords;//助记词
    private String address;//钱包地址
}
```

### 7.4 WalletEntity

```java
class WalletEntity {
	private String name;//钱包名称
    private String address;//钱包地址
}
```

### 7.5 BalanceEntity

```java
class BalanceEntity {
    private String name; //币种名称
    private String symbol; //币种代号
    private String addr; //钱包地址
    private String balance; //地址的此币种余额
    private String legalValue; //币种的法币价值
    private String conAddr; //币种合约地址
    private String decimals; //币种精度
    private String isToken;//是否为代币，true表示代币；false表示主链本币
    private String coinIcon; //币种图标
} 
```

### 7.6 AssetEntity

```java
class AssetEntity {
    private String coinType; //币种主链编号，第三方应用无需关心
    private String name; //币种的名称，基本上和合约里面的一致
    private String symbol; //币种的符号
    private String decimals;//币种精度
    private String coinIcon;//币种图标
    private String conAddr; //币种合约地址
}
```

### 7.7 AssetDetailEntity

```java
class AssetDetailEntity {
    private String name;//币种名称
    private String symbol;//币种符号
    private String addr; //地址
    private String balance;//币种余额数量
    private String conAddr;//币种合约地址
    private String coinIcon; //币种图片地址
    private String fee;//交易的旷工费
    private String legalValue;//币种小数点精度
}
```

### 7.8 TransactionRecord

```java
class TransactionRecord {
    public String from;//转出方地址
    public String to;//收款人地址
    public String conAddr;//币种合约地址
    public String value;//转账金额
    public String valueName;//转账币种名称
    public String fee;//手续费金额
    public String feeName;//手续费币种名称
    public String timeStamp;//转账时间戳 单位：秒
    public String blockN;//区块号
    public String txHash;//交易hash
    public String memo;//交易备注信息
    public String status; //交易是否成功，"0x1"表示成功
    public String modifyTime;//最后一次修改时间
}
```

### 7.9 OnExecCallback

```java
interface OnExecCallback {
	void onSuccess();//执行成功
	void onFail(int code,String message);//执行失败
}
```

### 7.10 KeyPairEntity

```java
class KeyPairEntity {
    private String priKey; //私钥
    private String pubKey; //公钥
}
```

### 7.11 SignResultEntity

```java
class SignResultEntity {
    private String pubKey; //公钥
    private String signature; //币种的名称，基本上和合约里面的一致
}
```

