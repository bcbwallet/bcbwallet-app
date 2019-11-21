bcb wallet DAPP接入文档
===================================

版本&更新记录
-----------

======= ========= ========== ========
版本号  作者      日期       更新内容
======= ========= ========== ========
v.1.0.0 bcbwallet 2019-07-15 初始版本
======= ========= ========== ========

背景
-----

<<<<<<< HEAD
为方便DAPP应用接入 bcb wallet 钱包，参与
BCB生态建设,整理成接口集成文档提供给开发者使用。开发者集成后可以利用 bcb
wallet钱包进行调试。
=======
本文档的主要阅读对象是面向bcb链开发DAPP的第三方开发者。
DAPP开发者只需要按照本文档的接口说明进行集成，就可以快速的完成DAPP接入到bcb wallet。
开发者集成后，还可以利用 bcb wallet 钱包进行调试。
>>>>>>> 173655afd2987c7b8e988541c716bec1fcfe6831

功能说明
-------

本文档提供钱包的DAPP访问接口说明。同时适用于Andriod/IOS。

方法：

.. code:: js

   bcbwallet('module.method', params, function(data){
       
   })

================ ========= ===============================
参数             类型      描述
================ ========= ===============================
module.method    string    module:模块 method:具体方法名
params           dictionry js 调用 app 时传递的参数
function(data){} callback  回调方法, data类型: json string
================ ========= ===============================

调试步骤：

​ 1.下载官方钱包 bcb wallet；

​ 2.调试 url 按照
bcbwallet://req_web=url规则生成二维码(如：bcbwallet://req_web=http://172.18.20.130:8000/jsapi/
)；

​ 3.打开 bcb wallet
钱包，首页右上角找到扫描二维码功能,然后扫描上述步骤生成的二维码进行调试。

官方钱包下载地址:\ https://www.bcbchain.io/down

H5demo
参考地址:\ https://github.com/bcbwallet/bcbwallet-app/tree/master/bcbwallet

Native
------

1.native.getVersionCode
~~~~~~~~~~~~~~~~~~~~~~~

获取bcb wallet 钱包的版本号

-  调用方式

.. code:: html

   bcbwallet('native.getVersionCode', null, callback);

-  callback

.. code:: html

   function(data) {
     //data: 返回钱包的版本号
   }

-  代码示例

::

   bcbwallet('native.getVersionCode', null, function (data) {
       alert(data);
   });

2.native.getVersionName
~~~~~~~~~~~~~~~~~~~~~~~~

获取 bcb wallet 钱包构建版本号

-  调用方式

.. code:: html

   bcbwallet('native.getVersionName', null, callback);

-  callback

.. code:: html

   function(data) {
      //data: 返回钱包的构建版本号
   }

-  代码示例

::

   bcbwallet('native.getVersionName', null, function (data) {
       alert(data);
   });

3.native.openUrl
~~~~~~~~~~~~~~~~~

通过此方法在 bcb wallet 钱包中打开一个新的 webview页面

-  调用方式

.. code:: html

   bcbwallet('native.openUrl', params, null);

-  params

.. code:: html

   {
     "url":"https://www.bcbscan.io/", //链接地址
     "title":"BCBScan", //页面标题
     "showTitle":true  //true为显示app 导航栏并显示title，false则隐藏app 导航栏
   }

-  代码示例

::

   bcbwallet('native.openUrl', {
       "url":"https://www.bcbscan.io/",
       "title":"BCBScan",
       "showTitle":true
   }, null);

4.native.goBack
~~~~~~~~~~~~~~~

调用此方法退出当前 webview 界面，回到 app界面

-  调用方式

.. code:: html

   bcbwallet('native.goBack', null, null);

5.native.scanQRCode
~~~~~~~~~~~~~~~~~~~~

调用此方法打开 bcb wallet 钱包的相机扫描二维码功能，并把扫码结果返回

-  调用方式

.. code:: html

   bcbwallet('native.scanQRCode', null, callback);

-  callback

.. code:: html

   function(data) {
   　//data: 扫描结果字符串
   }

-  代码示例

::

   bcbwallet('native.openUrl', null, function (data) {
       alert(data);
   });

6.native.screenChange
~~~~~~~~~~~~~~~~~~~~

调用此方法，可以设置不同的参数强制bcb wallet 钱包进行横竖屏或全屏操作

-  调用方式

.. code:: html

   bcbwallet('native.screenChange', params, null);

-  params

.. code:: html

   {
     "landType":"0", //横竖屏 0：竖屏，1：横屏
     "fullType":"0", //是否全屏显示 0：非全屏，1：全屏
   }

-  代码示例

::

   bcbwallet('native.screenChange', {
       "landType":"1",
       "fullType":"1"
   }, null);

BCB
---

1.bcb.getWalletsInfo
~~~~~~~~~~~~~~~~~~~~

调用此方法可以获取当前bcb wallet
钱包的所有钱包信息列表(钱包名称和钱包地址)

-  调用方式

.. code:: html

   bcbwallet('bcb.getWalletsInfo', null, callback);

-  callback

.. code:: html

   function(data) {
      data //所有钱包地址信息
   }
   ****返回钱包列表信息****
    data:[
            {
                "name":"myWallet",
                "walletAddr":"bcbPDTi68XwoMgGTwxd7ioZeMHHz7p7ewLtQ"
            },
            {
                "name":"newWallet",
                "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU"
            }
        ]

-  代码示例

::

   bcbwallet('native.getWalletsInfo', null, function (data) {
       alert(data);
   });

2.bcb.commonPayUrl
~~~~~~~~~~~~~~~~~~~~

调用此方法可以打开 bcb wallet
钱包显示当前支付信息，信息校验正确后可以进行支付操作,支付完成后返回支付的状态

-  调用方式

.. code:: html

   bcbwallet('bcb.commonPayUrl', params, callback);

-  params

::

   {
       "payUrl":"http://172.18.20.130:8000/bcbpay/" //支付订单链接
   }

-  callback

.. code:: html

   function(data) {
      //data: 返回交易hash
   }

-  代码示例

.. code:: js

   bcbwallet('bcb.commonPayUrl', {
     "payUrl":"http://172.18.20.156:8080/bcbtest/test2.txt"
   }, function (data) {
      alert(data);
      //"{  \"txHash\" : \"3E105CCAD994B5F1E8415086A1EA65B7420EDCCF8331D2EB02BC0B626EEF8A41\"}"
   });
3.bcb.commonPayParams
~~~~~~~~~~~~~~~~~~~~

调用此方法可以打开 bcb wallet
钱包显示当前支付信息，信息校验正确后可以进行支付操作，支付完成后返回支付的状态

-  调用方式

.. code:: html

   bcbwallet('bcb.commonPayParams', params, callback);

-  params

   ::

      {
        "ver": 3,
        "appUISeg": {
            "title": "通用支付",
            "value": "0.1",
            "referInfo": "进行支付操作",
            "symbol": "BCB"
          },
         "coinParams": {
         "note": "备注",
         "gasLimit": "25000",
         "calls": [{
          "contract": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
          "method": "Transfer(types.Address,bn.Number)",
          "params": ["bcbL8BzfVfcxtqh9umN3dUhxBYNyEnV7GiSa", "100000000"]
         }]
        }
      }

-  callback

.. code:: html

   function(data) {
      //data: 返回交易hash
   }

-  代码示例

.. code:: js

   bcbwallet('bcb.commonPayParams', params, function (data) {
       alert(data);
       //"{  \"txHash\" : \"3E105CCAD994B5F1E8415086A1EA65B7420EDCCF8331D2EB02BC0B626EEF8A41\"}"
   });

-  bcb wallet 钱包支付展示

   H5调用bcb.commonPayUrl 或 bcb.commonPayParams 方法时会唤起 bcb wallet钱包的支付页面，用户此时可以查看支付信息并进行支付操作。如下图所示
  
   .. image:: /_static/pay.png
    :scale: 30 %
    :alt: pay
    :align: center


4.bcb.signData
~~~~~~~~~~~~~~~~~~~~

调用此方法利用bcb wallet钱包的底层库进行数据签名，并把签名的数据返回

-  调用方式

.. code:: html

   bcbwallet('bcb.signData', params, callback);

-  params

::

   {
       "address":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU", //签名钱包地址
       "signContent":"test" //待签名内容
   }

-  callback

.. code:: html

   fnction(data) {
       data.type, //签名方式
       date.pubKey, //公钥
       data.signature //签名后内容
   }

-  代码示例

.. code:: js

   bcbwallet('bcb.signData', {
       "address":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU", //指定签名的钱包地址
       "signContent":"test"
   }, function (data) {
       alert(data);
   });

5.bcb.thirdAuth
~~~~~~~~~~~~~~~~~~~~

调用此方法进行 bcb wallet 钱包进行授权，并把授权状态返回

-  调用方式

.. code:: html

   bcbwallet('bcb.thirdAuth', params, callback);

-  params

   ::

      {
          "nonce":"cpNGXLhwjkVMXrrOvJj1UjwV8v2qftvM", //随机数
          "appID":"10", //业务ID
          "sessionInfo":"RFzLhUreEUM9eCAN0UEJXFXYYyvdctsU", //用户信息
          "address": "bcbi6Xt6356NuGxfGmmXm2kjPaQ9F1GefA2"  //指定钱包地址授权
      }

-  callback

.. code:: html

   function(data) {
   data.code, //0为授权成功
      data.message,
   }

-  代码示例

   ::

      bcbwallet('bcb.thirdAuth', {
          "nonce":"cpNGXLhwjkVMXrrOvJj1UjwV8v2qftvM",
          "appID":"10",
          "sessionInfo":"RFzLhUreEUM9eCAN0UEJXFXYYyvdctsU",
          "address": "bcbi6Xt6356NuGxfGmmXm2kjPaQ9F1GefA2"
      }, function (data) {
          alert(data);
      });

<<<<<<< HEAD
=======
OTC
---

1.otc.openOtc
~~~~~~~~~~~~~~~~~~~~

调用此方法进入bcb wallet 钱包的OTC模块

-  调用方式

.. code:: html

   bcbwallet('otc.openOtc', null, null);

2.otc.openFastExchange
~~~~~~~~~~~~~~~~~~~~

调用此方法进入bcb wallet 钱包的闪兑模块

-  调用方式

.. code:: html

   bcbwallet('otc.openFastExchange', params, null);

-  params

::

   {
       "inCoin":"DC", //待兑换币种
       "outCoin":"USDX", //目标兑换币种
       "autoFinish":true
   }

-  代码示例

.. code:: html

   bcbwallet('otc.openFastExchange', {
       "inCoin":"DC",
       "outCoin":"USDX",
       "autoFinish":true
   }, null);
>>>>>>> 173655afd2987c7b8e988541c716bec1fcfe6831
