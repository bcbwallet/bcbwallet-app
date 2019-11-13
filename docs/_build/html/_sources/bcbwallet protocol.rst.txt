bcbwallet://相关协议说明
========================

版本更新
--------

====== ========= ========= ========
版本号 作者      日期      更新内容
====== ========= ========= ========
v1.0   bcbwallet 2019-11-7 初始版本
====== ========= ========= ========

1.支付协议
----------

::

   bcbwallet://req_pay=支付链接

协议说明:通过此协议拉起 bcbwallet 的支付功能,并把支付hash 返回.

示例代码:

.. code:: js

   url = "bcbwallet://req_pay=https://testclt.cgs.cool/yeb/h5/bcb/investment/transfer/jcsd0IB7g444P9UyhyXsggqHfDOtuK6A"
   jsbridge(url);
   window.inform = function(d) {
       if(d.txHash) {
         console.log(d.txHash);
        } else {
         console.log("fail");
        }
      }

返回结果:

支付完成后, 如果存在txHash, 可根据 txHash
值查询支付详情,否则视为支付失败.

2.授权认证协议
--------------

::

   bcbwallet://req_auth=授权链接

协议说明:通过此协议唤起bcbwallet 的授权功能.

示例代码:

.. code:: js

    url = "bcbwallet://req_auth=https://clt.cgs.cool/otc/callback/token/nE74Lya9Oa4Z6H1a6hvPL9ntOiv2ot1v"
   jsbridge(url);

3.获取钱包列表
--------------

::

   bcbwallet://req_info=bcbinforeq

协议说明:通过此协议获取 bcbwallet 所有的钱包地址的 json 字符串.

示例代码:

.. code:: js

   jsbridge("bcbwallet://req_info=bcbinforeq");
   window.inform = function(walletsJson) {
       console.log(walletsJson);
      }

返回结果:

返回钱包列表的 json 字符串.

4.打开普通 web页面
------------------

::

   bcbwallet://req_web=h5链接

协议说明:通过此协议在 bcbwallet 钱包内部打开链接页面

示例代码:

.. code:: js

   jsbridge("bcbwallet://req_web=https://www.bcbscan.io");

5.启动扫码功能
--------------

::

   bcbwallet://req_info=qrcode

协议说明:通过此协议唤起 bcbwallet 的二维码扫码功能,并把扫码识别结果返回.

示例代码:

.. code:: js

   jsbridge("bcbwallet://req_info=qrcode");
   window.inform = function(qrCode) {
       console.log(qrCode);
      }

返回结果:返回二维码扫描的识别结果.

6.退出 web页面
--------------

::

   bcbwallet://req_info=exitpage

协议说明:通过此协议可以强制退出当前的h5页面返回 iOS/Android 界面

示例代码:

.. code:: js

   jsbridge("bcbwallet://req_info=exitpage");

7.竖屏操作
----------

::

   bcbwallet://req_info=portscreen

协议说明:通过此协议可以在h5页面强制 app竖屏.

示例代码:

.. code:: js

   jsbridge("bcbwallet://req_info=portscreen");

8.横屏操作
----------

::

   bcbwallet://req_info=landscreen

协议说明:通过此协议可以在h5页面强制 app横屏.

示例代码:

.. code:: js

   jsbridge("bcbwallet://req_info=landscreen");

9.全屏操作
----------

::

   bcbwallet://req_info=fullscreen

协议说明:通过此协议可以在h5页面强制 app全屏.

示例代码:

.. code:: js

   jsbridge("bcbwallet://req_info=fullscreen");

通用方法
--------

.. code:: js

   const jsbridge = function (urlData) {
       let device = Device()
       if (!urlData.includes('://')) urlData = 'bcbwallet://' + urlData
       if (device == 'Android' || device == 'WindowsPhone') {
           let iframe = document.createElement('iframe')
           iframe.style.width = '1px'
           iframe.style.height = '1px'
           iframe.style.display = 'none'
           iframe.src = urlData
           document.body.appendChild(iframe)
           setTimeout(function () {
               iframe.remove()
           }, 100)
       } else if (device == 'iPhone') {
           try {
               window.webkit.messageHandlers.BCBPay.postMessage(urlData)
           } catch (e) {}
       }
   }