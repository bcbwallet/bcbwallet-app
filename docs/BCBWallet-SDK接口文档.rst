{\rtf1\ansi\ansicpg936\cocoartf1671\cocoasubrtf500
{\fonttbl\f0\fnil\fcharset134 PingFangSC-Regular;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red38\green38\blue38;\red242\green242\blue242;}
{\*\expandedcolortbl;;\cssrgb\c20000\c20000\c20000;\cssrgb\c96078\c96078\c96078;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \'c7\'ae\'b0\'fc
\f1 SDK
\f0 \'bd\'d3\'bf\'da\'ce\'c4\'b5\'b5\'cb\'b5\'c3\'f7
\f1 \
===================\
\

\f0 \'b0\'e6\'b1\'be
\f1 &
\f0 \'b8\'fc\'d0\'c2\'bc\'c7\'c2\'bc
\f1 \
=============\
\
======= ========= ========== ============\

\f0 \'b0\'e6\'b1\'be\'ba\'c5
\f1   
\f0 \'d7\'f7\'d5\'df
\f1       
\f0 \'c8\'d5\'c6\'da
\f1        
\f0 \'b8\'fc\'d0\'c2\'c4\'da\'c8\'dd
\f1 \
======= ========= ========== ============\
v.1.0.0 bcbwallet 2019-04-01 
\f0 \'b3\'f5\'ca\'bc\'b0\'e6\'b1\'be
\f1 \
v.1.0.1 bcbwallet 2019-06-24 
\f0 \'cd\'c6\'cb\'cd\'c4\'a3\'bf\'e9
\f1 \
v.1.0.2 bcbwallet 2019-07-01 bcbwallet2.0\
v.1.0.3 bcbwallet 2019-10-23 
\f0 \'d0\'c2\'d4\'f6\'b2\'e0\'c1\'b4\'c7\'ae\'b0\'fc
\f1 \
======= ========= ========== ============\
\
--------------\
\
--------------\
\

\f0 \'b9\'a6\'c4\'dc\'cb\'b5\'c3\'f7
\f1 \
========\
\

\f0 \'b1\'be\'ce\'c4\'b5\'b5\'cc\'e1\'b9\'a9\'c7\'ae\'b0\'fc\'b5\'c4
\f1 SDK
\f0 \'b7\'c3\'ce\'ca\'bd\'d3\'bf\'da\'cb\'b5\'c3\'f7\'a1\'a3
\f1 IOS
\f0 \'b0\'e6\'b1\'be\'a1\'a3
\f1 \
\

\f0 \'bd\'d3\'bf\'da\'b7\'c3\'ce\'ca\'b7\'bd\'ca\'bd
\f1 \
============\
\
API
\f0 \'b5\'f7\'d3\'c3\'a3\'ac\'b7\'b5\'bb\'d8\'b5\'c4\'c4\'da\'c8\'dd\'d2\'b2\'ca\'c7\'d2\'bb\'b8\'f6
\f1 json
\f0 \'b4\'ae\'a3\'ac\'c0\'ef\'c3\'e6\'bb\'e1\'d0\'af\'b4\'f8\'b7\'b5\'bb\'d8\'b5\'c4\'d7\'b4\'cc\'ac
\f1 \

\f0 \'c2\'eb\'d2\'d4\'bc\'b0\'d2\'bb\'d0\'a9\'b7\'b5\'bb\'d8\'b5\'c4\'b1\'d8\'d2\'aa\'b2\'ce\'ca\'fd\'a1\'a3
\f1 \
\
1.
\f0 \'b3\'f5\'ca\'bc\'bb\'af\'c9\'e8\'d6\'c3
\f1 \
============\
\
1.
\f0 \'d7\'a2\'b2\'e1
\f1 APP\
---------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**+ (BOOL)registerApp:(NSString )appid pushID:(NSString)pushid;**\
\
**
\f0 \'ca\'e4\'c8\'eb\'b2\'ce\'ca\'fd\'cb\'b5\'c3\'f7
\f1 **\
\
====== ====== ==== ===========================\

\f0 \'b2\'ce\'ca\'fd\'c3\'fb
\f1  
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
====== ====== ==== ===========================\
appid  string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'ba\'f3\'cc\'a8\'b7\'d6\'c5\'e4\'b8\'f8\'b5\'da\'c8\'fd\'b7\'bd\'b5\'c4
\f1 APPID\
pushid string 
\f0 \'ca\'c7
\f1    
\f0 \'b5\'da\'c8\'fd\'b7\'bd\'bd\'d3\'c8\'eb\'b5\'c4\'cd\'c6\'cb\'cd
\f1 ID\
====== ====== ==== ===========================\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d7\'a2\'b2\'e1\'b3\'c9\'b9\'a6
\f1 **\
\
.. code:: java\
\
   return YES;\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d7\'a2\'b2\'e1\'ca\'a7\'b0\'dc
\f1 **\
\
.. code:: java\
\
   return NO;\
\
2.
\f0 \'d3\'ef\'d1\'d4\'c9\'e8\'d6\'c3
\f1 \
----------\
\
+ (**void**)setLanguage:(NSString \\*)language;\
''''''''''''''''''''''''''''''''''''''''''''''\
\
**
\f0 \'ca\'e4\'c8\'eb\'b2\'ce\'ca\'fd\'cb\'b5\'c3\'f7
\f1 **\
\
======== ====== ==== ======================================================\

\f0 \'b2\'ce\'ca\'fd\'c3\'fb
\f1    
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
======== ====== ==== ======================================================\
language string 
\f0 \'ca\'c7
\f1    SDK
\f0 \'d6\'d0
\f1 API
\f0 \'b7\'b5\'bb\'d8
\f1 msg
\f0 \'d3\'ef\'d1\'d4\'c0\'e0\'d0\'cd\'a3\'a8
\f1 \\ *cn
\f0 \'a3\'ba\'d6\'d0\'ce\'c4\'a1\'a2
\f1 en
\f0 \'a3\'ba
\f1 English*\\ 
\f0 \'a3\'a9
\f1 \
======== ====== ==== ======================================================\
\
3.
\f0 \'bf\'aa\'b7\'a2\'bb\'b7\'be\'b3\'c9\'e8\'d6\'c3
\f1 \
--------------\
\
-(**void**)setWalletDebug:(ICRunType)walletDebug OTCDebug:(ICRunType)otcDebug;\
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\
\
**
\f0 \'ca\'e4\'c8\'eb\'b2\'ce\'ca\'fd\'cb\'b5\'c3\'f7
\f1 **\
\
=========== ==== ==== ============================================================\

\f0 \'b2\'ce\'ca\'fd\'c3\'fb
\f1       
\f0 \'c0\'e0\'d0\'cd
\f1  
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
=========== ==== ==== ============================================================\
walletDebug int  
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b9\'dc\'c0\'ed\'c1\'b4\'bb\'b7\'be\'b3\'a3\'a8
\f1 \\ *0
\f0 \'a3\'ba\'d1\'d0\'b7\'a2\'c1\'b4\'a1\'a2
\f1 1
\f0 \'a3\'ba\'b2\'e2\'ca\'d4\'c1\'b4\'a1\'a2
\f1 2
\f0 \'a3\'ba\'d5\'fd\'ca\'bd\'c1\'b4
\f1 *\\ 
\f0 \'a3\'a9
\f1 \
otcDebug    int  
\f0 \'ca\'c7
\f1    OTC
\f0 \'bc\'b0\'c9\'c1\'b6\'d2\'c4\'a3\'bf\'e9\'c1\'b4\'bb\'b7\'be\'b3\'a3\'a8
\f1 \\ *0
\f0 \'a3\'ba\'d1\'d0\'b7\'a2\'c1\'b4\'a1\'a2
\f1 1
\f0 \'a3\'ba\'b2\'e2\'ca\'d4\'c1\'b4\'a1\'a2
\f1 2
\f0 \'a3\'ba\'d5\'fd\'ca\'bd\'c1\'b4
\f1 *\\ 
\f0 \'a3\'a9
\f1 \
=========== ==== ==== ============================================================\
\
4.
\f0 \'bb\'f1\'c8\'a1\'d6\'f7\'c1\'b4\'bc\'b0\'cb\'f9\'d3\'d0\'b2\'e0\'c1\'b4\'d0\'c5\'cf\'a2
\f1 \
------------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
-(**void**)loadAllChainsFinish:(\\ **void**\\ (^)(ICSDKResultModel \\*\
result))finish;\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -1:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \{\
           "devtest":["http://103.17.30.84:46657"],\
           "sctest":["http://103.17.30.85:46657/sctest"]\
       \}\
   \}\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1,\
       "msg": "error",\
       "result":\{\}\
   \}\
\
5.
\f0 \'c1\'b4\'bb\'b7\'be\'b3\'c9\'e8\'d6\'c3
\f1 \
------------\
\
\\**-(void)setWalletChain:(NSString \\*)chainId;*\\*\
'''''''''''''''''''''''''''''''''''''''''''''''''\
\
**
\f0 \'ca\'e4\'c8\'eb\'b2\'ce\'ca\'fd\'cb\'b5\'c3\'f7
\f1 **\
\
======= ====== ==== ================================\

\f0 \'b2\'ce\'ca\'fd\'c3\'fb
\f1   
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
======= ====== ==== ================================\
chainId string 
\f0 \'ca\'c7
\f1    
\f0 \'c1\'b4
\f1 ID
\f0 \'a3\'ac\'b4\'ab\'bf\'d5\'d7\'d6\'b7\'fb\'b4\'ae\'d4\'f2\'d6\'d8\'d6\'c3\'ce\'aa\'d6\'f7\'c1\'b4\'bd\'da\'b5\'e3
\f1 \
======= ====== ==== ================================\
\
6.
\f0 \'bb\'f1\'c8\'a1\'c1\'b4\'bb\'b7\'be\'b3\'b6\'d4\'d3\'a6\'b5\'c4\'cd\'f8\'c2\'e7\'bd\'da\'b5\'e3
\f1 \
--------------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -2:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
-(**void**)loadChainNodesFinish:(\\ **void**\\ (^)(ICSDKResultModel \\*\
result))finish;\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -2:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": [\
           \{\
               "name":"devwallet",\
               "urlType":0,\
               "url":"http://172.18.10.78/sctest2"\
           \},\
          \{\
              "name":"http://148.66.11.75:46657",\
              "urlType":1,\
              "url":"http://148.66.11.75:46657"\
          \}\
       ]\
   \}\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1,\
       "msg": "error",\
       "result":\{\}\
   \}\
\
7.
\f0 \'bd\'da\'b5\'e3\'c9\'e8\'d6\'c3
\f1 \
----------\
\
\\**-(void)setNodeUrl:(NSString \\*)nodeUrl nodeType:(NSInteger)nodeType;*\\*\
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\
\
**
\f0 \'ca\'e4\'c8\'eb\'b2\'ce\'ca\'fd\'cb\'b5\'c3\'f7
\f1 **\
\
======== ====== ==== ====================================\

\f0 \'b2\'ce\'ca\'fd\'c3\'fb
\f1    
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
======== ====== ==== ====================================\
nodeUrl  string 
\f0 \'ca\'c7
\f1    
\f0 \'cd\'f8\'c2\'e7\'bd\'da\'b5\'e3\'a3\'ac\'b4\'ab\'bf\'d5\'d7\'d6\'b7\'fb\'b4\'ae\'d4\'f2\'d6\'d8\'d6\'c3\'ce\'aa\'c4\'ac\'c8\'cf\'bd\'da\'b5\'e3
\f1 \
nodeType int    
\f0 \'ca\'c7
\f1    
\f0 \'bd\'da\'b5\'e3\'c0\'e0\'d0\'cd
\f1 \
======== ====== ==== ====================================\
\
2.
\f0 \'c7\'ae\'b0\'fc\'b9\'dc\'c0\'ed
\f1 \
==========\
\
1.
\f0 \'b4\'b4\'bd\'a8\'d0\'c2\'c7\'ae\'b0\'fc
\f1 \
------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
-(**void**)createWallet:(NSString *)name password:(NSString*)password recommend:(NSString *)recommend finish:(\\ *\\ **void**\\ *\\ (^)(ICSDKResultModel* result))finish;\
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\
\
**
\f0 \'ca\'e4\'c8\'eb\'b2\'ce\'ca\'fd\'cb\'b5\'c3\'f7
\f1 **\
\
========= ====== ==== ================\

\f0 \'b2\'ce\'ca\'fd\'c3\'fb
\f1     
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========= ====== ==== ================\
name      string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
password  string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
recommend string 
\f0 \'b7\'f1
\f1    
\f0 \'cd\'c6\'bc\'f6\'c8\'cb\'b5\'c4\'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========= ====== ==== ================\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{\
           "name":"myWallet",\
           "mnemonicWords":"eyebrow indoor orbit cinnamon hour gain category spawn walk bind spread clinic",       \
           "walletAddr":"bcbPDTi68XwoMgGTwxd7ioZeMHHz7p7ewLtQ"\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
============= ====== ========================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1         
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
============= ====== ========================\
name          string 
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
mnemonicWords string 
\f0 \'c7\'ae\'b0\'fc\'b5\'c4\'d6\'fa\'bc\'c7\'b4\'ca\'a3\'ac\'bf\'d5\'b8\'f1\'d7\'f6\'b7\'d6\'b8\'ee
\f1 \
walletAddr    string 
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
============= ====== ========================\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'b4\'b4\'bd\'a8\'c7\'ae\'b0\'fc\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
2.
\f0 \'b5\'bc\'c8\'eb\'cb\'bd\'d4\'bf\'c9\'fa\'b3\'c9\'c7\'ae\'b0\'fc
\f1 \
------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)importPrivateKey:(NSString )name key:(NSString)key\
password:(NSString )password recommend:(NSString)recommend\
finish:(void(^)(ICSDKResultModel \\* result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========= ====== ==== ================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1     
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========= ====== ==== ================\
name      string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
key       string 
\f0 \'ca\'c7
\f1    
\f0 \'cb\'bd\'d4\'bf
\f1 \
password  string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
recommend string 
\f0 \'b7\'f1
\f1    
\f0 \'cd\'c6\'bc\'f6\'c8\'cb\'b5\'c4\'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========= ====== ==== ================\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -1:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{   \
           "name":"myWallet",\
           "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ========\
name       string 
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
walletAddr string 
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ========\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'b5\'bc\'c8\'eb\'c7\'ae\'b0\'fc\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
3.
\f0 \'b5\'bc\'c8\'eb
\f1 Keystore
\f0 \'c9\'fa\'b3\'c9\'c7\'ae\'b0\'fc
\f1 \
----------------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)importKeystore:(NSString )name key:(NSString)key\
password:(NSString )password recommend:(NSString)recommend\
finish:(void(^)(ICSDKResultModel \\* result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========= ====== ==== ================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1     
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========= ====== ==== ================\
name      string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
key       string 
\f0 \'ca\'c7
\f1    Keystore\
password  string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
recommend string 
\f0 \'b7\'f1
\f1    
\f0 \'cd\'c6\'bc\'f6\'c8\'cb\'b5\'c4\'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========= ====== ==== ================\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{   \
           "name":"myWallet",\
           "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ========\
name       string 
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
walletAddr string 
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ========\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'b5\'bc\'c8\'eb\'c7\'ae\'b0\'fc\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
4.
\f0 \'b5\'bc\'c8\'eb\'d6\'fa\'bc\'c7\'b4\'ca\'c9\'fa\'b3\'c9\'c7\'ae\'b0\'fc
\f1 \
--------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)importMnemonicWords:(NSString )name key:(NSString)key\
password:(NSString )password recommend:(NSString)recommend\
finish:(void(^)(ICSDKResultModel \\* result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========= ====== ==== ================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1     
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========= ====== ==== ================\
name      string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
key       string 
\f0 \'ca\'c7
\f1    
\f0 \'d6\'fa\'bc\'c7\'b4\'ca
\f1 \
password  string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
recommend string 
\f0 \'b7\'f1
\f1    
\f0 \'cd\'c6\'bc\'f6\'c8\'cb\'b5\'c4\'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========= ====== ==== ================\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -1:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{   \
           "name":"myWallet",\
           "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ========\
name       string 
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
walletAddr string 
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ========\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'b5\'bc\'c8\'eb\'c7\'ae\'b0\'fc\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
5.
\f0 \'bb\'f1\'c8\'a1\'cb\'f9\'d3\'d0\'c7\'ae\'b0\'fc\'d0\'c5\'cf\'a2
\f1 \
------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -2:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
\\**-(ICSDKResultModel \\*)getWallets;*\\*\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -2:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       [\
           \{\
               "name":"myWallet",\
               "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"\
           \},\
           \{\
               "name":"newWallet",\
               "walletAddr":"bcbCUh7Zsb7PBgLwHJVok2QaMhbW64HNK4FU"\
           \}\
       ]\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ========\
name       string 
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
walletAddr string 
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ========\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'bb\'f1\'c8\'a1\'c7\'ae\'b0\'fc\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
6.
\f0 \'c7\'ae\'b0\'fc\'cd\'c6\'cb\'cd\'b0\'f3\'b6\'a8\'d7\'b4\'cc\'ac
\f1 \
------------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**- (**\\ BOOL)hasBindPushID:(NSString \\*)walletAddr;\
\
**
\f0 \'ca\'e4\'c8\'eb\'b2\'ce\'ca\'fd\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'b2\'ce\'ca\'fd\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ==== ========\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d2\'d1\'b0\'f3\'b6\'a8
\f1 **\
\
.. code:: java\
\
   return YES;\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'ce\'b4\'b0\'f3\'b6\'a8
\f1 **\
\
.. code:: java\
\
   return NO;\
\
7.
\f0 \'b0\'f3\'b6\'a8\'c7\'ae\'b0\'fc\'cd\'c6\'cb\'cd
\f1 \
--------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**\'96(**\\ void\\ **)bindWalletPush:(NSString )walletAddr\
finish:(\\ \\ void\\ \\ (^)(ICSDKResultModel result))finish;**\
\
**
\f0 \'ca\'e4\'c8\'eb\'b2\'ce\'ca\'fd\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'b2\'ce\'ca\'fd\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ==== ========\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -1:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \{\}\
   \}\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'cd\'c6\'cb\'cd\'d7\'a2\'b2\'e1\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
8.
\f0 \'b5\'bc\'b3\'f6\'d6\'fa\'bc\'c7\'b4\'ca
\f1 \
------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -2:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)getMnemonicWords:(NSString )walletAddr\
password:(NSString)password finish:(void(^)(ICSDKResultModel \\*\
result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
password   string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
========== ====== ==== ========\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -2:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{\
           "mnemonicWords":"eyebrow indoor orbit cinnamon hour gain category spawn walk bind spread clinic",       \
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
============= ====== ============\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1         
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
============= ====== ============\
mnemonicWords string 
\f0 \'c7\'ae\'b0\'fc\'b5\'c4\'d6\'fa\'bc\'c7\'b4\'ca
\f1 \
============= ====== ============\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'bb\'f1\'c8\'a1\'d6\'fa\'bc\'c7\'b4\'ca\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
9.
\f0 \'b5\'bc\'b3\'f6\'cb\'bd\'d4\'bf
\f1 \
----------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -3:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)exportPrivateKey:(NSString )walletAddr\
password:(NSString)password finish:(void(^)(ICSDKResultModel \\*\
result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
password   string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
========== ====== ==== ========\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -3:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{                "privateKey":"0x98BB2E49822A48728E3CBCFD1A933C1FC500A6204453E7DB85F84EFB90146600"\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ========\
privateKey string 
\f0 \'c3\'f7\'ce\'c4\'cb\'bd\'d4\'bf
\f1 \
========== ====== ========\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'b5\'bc\'b3\'f6\'cb\'bd\'d4\'bf\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
10.
\f0 \'b5\'bc\'b3\'f6
\f1 Keystore\
---------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)exportKeystore:(NSString )walletAddr\
password:(NSString)password finish:(void(^)(ICSDKResultModel \\*\
result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
password   string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
========== ====== ==== ========\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code": 0,\
       "msg": "ok",\
       "result": \{\
           "keystore": "\{\\"address\\":\\"bcbMd6xUDQLoivMT45Qp8o7M8vjN5wRyHAF3\\",\\"crypto\\":\{\\"cipher\\":\\"aes-128-ctr\\",\\"cipherparams\\":\{\\"iv\\":\\"026fad88d89baadb9110ae533ef8039d\\"\},\\"ciphertext\\":\\"7c1dafc7e541cc14d0fe11773fc4d2da6933384d5279984df57693f98d3be4a8\\",\\"kdf\\":\\"scrypt\\",\\"kdfparams\\":\{\\"dklen\\":32,\\"n\\":262144,\\"p\\":1,\\"r\\":8,\\"salt\\":\\"c1fe07bed958a78763ac5816c7dbad9351accd80c18bbc70aa3279d5fb34638f\\"\},\\"mac\\":\\"d6042cf16b55c3bac25f392d1d33476e84e5276b672ad8e77ccd1713d586e18d\\"\},\\"id\\":\\"eabffab4-5c21-46a4-a709-9699a72d1339\\",\\"version\\":3\}"\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
======== ====== ============\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1    
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
======== ====== ============\
keystore string 
\f0 \'c3\'f7\'ce\'c4
\f1 keystore\
======== ====== ============\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'b5\'bc\'b3\'f6
\f1 keystore
\f0 \'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
11.
\f0 \'d1\'e9\'d6\'a4\'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
---------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)verifyPassword:(NSString )walletAddr\
password:(NSString)password finish:(void(^)(ICSDKResultModel \\*\
result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
password   string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
========== ====== ==== ========\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -1:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \{\}\
   \}\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'c3\'dc\'c2\'eb\'b4\'ed\'ce\'f3
\f1 ",\
       "result":\{\}\
   \}\
\
12.
\f0 \'d0\'de\'b8\'c4\'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb\'a3\'a8\'d6\'f7\'c1\'b4\'c7\'ae\'b0\'fc\'b6\'d4\'d3\'a6\'b5\'c4\'cb\'f9\'d3\'d0\'b2\'e0\'c1\'b4\'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb\'ce\'a8\'d2\'bb\'a3\'a9
\f1 \
-----------------------------------------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -2:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)changePassword:(NSString )walletAddr\
oldPassword:(NSString)oldPassword newPassword:(NSString )newPassword\
finish:(void(^)(ICSDKResultModel result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
=========== ====== ==== ==========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1       
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
=========== ====== ==== ==========\
walletAddr  string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
oldPassword string 
\f0 \'ca\'c7
\f1    
\f0 \'d4\'ad\'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
newPassword string 
\f0 \'ca\'c7
\f1    
\f0 \'d0\'c2\'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
=========== ====== ==== ==========\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -2:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \{\}\
   \}\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'d4\'ad\'c3\'dc\'c2\'eb\'ca\'e4\'c8\'eb\'b4\'ed\'ce\'f3
\f1 ",\
       "result":\{\}\
   \}\
\
13.
\f0 \'d0\'de\'b8\'c4\'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6\'a3\'a8\'d6\'f7\'c1\'b4\'c7\'ae\'b0\'fc\'b6\'d4\'d3\'a6\'b5\'c4\'cb\'f9\'d3\'d0\'b2\'e0\'c1\'b4\'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6\'ce\'a8\'d2\'bb\'a3\'a9
\f1 \
-----------------------------------------------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)changeWalletName:(NSString )walletAddr\
newName:(NSString)newName finish:(void(^)(ICSDKResultModel \\*\
result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ==========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ==========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
newName    string 
\f0 \'ca\'c7
\f1    
\f0 \'d0\'c2\'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
========== ====== ==== ==========\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \{\
           "name":"newWallet",\
           "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5",\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ========\
name       string 
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6
\f1 \
walletAddr string 
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ========\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'c7\'ae\'b0\'fc\'c3\'fb\'b3\'c6\'b8\'f1\'ca\'bd\'b4\'ed\'ce\'f3
\f1 ",\
       "result":\{\}\
   \}\
\
14.
\f0 \'c9\'be\'b3\'fd\'c7\'ae\'b0\'fc\'a3\'a8\'d6\'f7\'c1\'b4\'c7\'ae\'b0\'fc\'b6\'d4\'d3\'a6\'b5\'c4\'c6\'e4\'cb\'fb\'b2\'e0\'c1\'b4\'c7\'ae\'b0\'fc\'cd\'ac\'b2\'bd\'c9\'be\'b3\'fd\'a3\'a9
\f1 \
-------------------------------------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)deleteWallet:(NSString )walletAddr password:(NSString)password\
finish:(void(^)(ICSDKResultModel \\* result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
password   string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
========== ====== ==== ========\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -1:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \{\}\
   \}\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'c3\'dc\'c2\'eb\'b4\'ed\'ce\'f3
\f1 ",\
       "result":\{\}\
   \}\
\
3.
\f0 \'d6\'a7\'b8\'b6\'bc\'b0\'bd\'bb\'d2\'d7\'b2\'e9\'d1\'af
\f1 \
================\
\
1.
\f0 \'c7\'ae\'b0\'fc\'d7\'aa\'d5\'cb
\f1 \
----------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -2:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)walletTransation:(NSString )walletAddr\
password:(NSString)password coinAddr:(NSString )coinAddr\
toAddr:(NSString)toAddr value:(NSString )value note:(NSString)note\
byb:(**\\ BOOL\\ **)byb finish:(void(^)(ICSDKResultModel \\*\
result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== =================================================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== =================================================\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
password   string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
coinAddr   string 
\f0 \'ca\'c7
\f1    
\f0 \'d2\'aa\'d7\'aa\'d5\'cb\'b1\'d2\'d6\'d6\'b5\'c4\'ba\'cf\'d4\'bc\'b5\'d8\'d6\'b7
\f1 \
toAddr     string 
\f0 \'ca\'c7
\f1    
\f0 \'d7\'aa\'d5\'cb\'b5\'bd\'b5\'c4\'c4\'bf\'b1\'ea\'b5\'d8\'d6\'b7
\f1 \
value      string 
\f0 \'ca\'c7
\f1    
\f0 \'d7\'aa\'d5\'cb\'b5\'c4\'bd\'f0\'b6\'ee\'a3\'ac\'c0\'fd\'c8\'e7
\f1 \'93102.23\'94\
note       string 
\f0 \'b7\'f1
\f1    
\f0 \'d7\'aa\'d5\'cb\'b5\'c4\'b1\'b8\'d7\'a2\'a3\'ac\'b6\'d4\'d3\'da
\f1 BCB
\f0 \'c1\'b4\'a3\'ac\'d5\'e2\'b8\'f6\'d7\'d6\'b6\'ce\'d7\'ee\'d6\'d5\'bb\'e1\'d0\'b4\'c8\'eb\'b5\'bd\'c7\'f8\'bf\'e9\'d6\'d0
\f1 \
byb        string 
\f0 \'ca\'c7
\f1    
\f0 \'ca\'c7\'b7\'f1\'ce\'aa
\f1 BYB
\f0 \'d7\'aa\'d5\'cb
\f1 \
========== ====== ==== =================================================\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -2:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{   \
           "txHash":"0x0F8642968E48A16316CD499BF142E15EEFF03BE44816796AF87DDC2F1B72BBA4",\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
====== ====== ================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1  
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
====== ====== ================\
txHash string 
\f0 \'d7\'aa\'d5\'cb\'b5\'c4\'c1\'b4\'c9\'cf
\f1 hash
\f0 \'d6\'b5
\f1 \
====== ====== ================\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'d7\'aa\'d5\'cb\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
2.
\f0 \'cd\'a8\'d3\'c3\'d6\'a7\'b8\'b6
\f1 -
\f0 \'cd\'a8\'d3\'c3\'d0\'cd\'ba\'cf\'d4\'bc\'d6\'a7\'b8\'b6\'bd\'d3\'bf\'da
\f1 \
-----------------------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)walletCommonPay:(NSString )walletAddr\
version:(\\ \\ int\\ )version password:(NSString)password\
walletCall:(NSString )walletCall finish:(void(^)(ICSDKResultModel\
result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== =============================================================================================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== =============================================================================================\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
version    Int    
\f0 \'ca\'c7
\f1    1.0
\f0 \'b5\'c4\'d6\'a7\'b8\'b6\'b4\'ab
\f1 1
\f0 \'a3\'ac
\f1  2.0
\f0 \'b5\'c4\'d6\'a7\'b8\'b6\'b4\'ab
\f1 2\
password   string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'c3\'dc\'c2\'eb
\f1 \
walletCall string 
\f0 \'ca\'c7
\f1    json
\f0 \'b4\'ae\'a3\'ac\'b4\'cb\'d7\'d6\'b6\'ce\'b8\'f9\'be\'dd\'b2\'bb\'cd\'ac\'b5\'c4\'ba\'cf\'d4\'bc\'b6\'a8\'d2\'e5\'d3\'d0\'b2\'bb\'cd\'ac\'b5\'c4\'ca\'fd\'be\'dd\'b8\'f1\'ca\'bd\'a3\'bb\'be\'df\'cc\'e5\'c7\'eb\'b2\'ce\'bc\'fb\'a1\'b6
\f1 BCB
\f0 \'c7\'ae\'b0\'fc\'cd\'a8\'d3\'c3\'d6\'a7\'b8\'b6\'bd\'d3\'c8\'eb\'b9\'e6\'b7\'b6\'a1\'b7\'d7\'dc\'c3\'e8\'ca\'f6
\f1 \
========== ====== ==== =============================================================================================\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba
\f1 walletCall
\f0 \'d7\'d6\'b7\'fb\'b4\'ae\'b8\'f1\'ca\'bd
\f1 **\
\
.. code:: java\
\
   "\{\\"walletCall\\":\{\\"conAddr\\":\\"bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9\\",\\"methodName\\":\\"BuyXid\\",\\"methodParam\\":[\{\\"name\\":\\"_affCode\\",\\"type\\":\\"int64\\",\\"value\\":\\"12345678\\"\},\{\\"name\\":\\"_team\\",\\"type\\":\\"int64\\",\\"value\\":\\"0\\"\},\{\\"name\\":\\"_bcb\\",\\"type\\":\\"Number-decimal\\",\\"value\\":\\"2.5\\"\}],\\"methodRet\\":\\"smc.Error\\"\}\}"\
\
**
\f0 \'ca\'be\'c0\'fd\'a3\'ba\'d5\'b9\'bf\'aa\'ba\'f3\'b5\'c4\'b8\'f1\'ca\'bd
\f1 **\
\
.. code:: java\
\
   \{   \
           "walletCall":\
           \{\
               "conAddr":"bcbLTwDzzZn3Jy8cJGvygWLgpTr9hEdVpWZ9",\
               "methodName":"BuyXid",\
               "methodParam":\
               [\
                   \{\
                       "name":"_affCode",\
                       "type":"int64",\
                       "value":"12345678"\
                   \},\
                   \{\
                       "name":"_team",\
                       "type":"int64",\
                       "value":"0"\
                   \},\
                   \{\
                       "name":"_bcb",\
                       "type":"Number-decimal",\
                       "value":"2.5"\
                   \}\
               ],\
               "methodRet":"smc.Error"\
           \}\
   \}\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{   \
           "txHash":"0x0F8642968E48A16316CD499BF142E15EEFF03BE44816796AF87DDC2F1B72BBA4"\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
====== ====== ================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1  
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
====== ====== ================\
txHash string 
\f0 \'d7\'aa\'d5\'cb\'b5\'c4\'c1\'b4\'c9\'cf
\f1 hash
\f0 \'d6\'b5
\f1 \
====== ====== ================\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'d6\'a7\'b8\'b6\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
3.
\f0 \'b2\'e9\'d1\'af\'d6\'b8\'b6\'a8\'b5\'d8\'d6\'b7\'d7\'ca\'b2\'fa
\f1 \
------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)getAddrsBalance:(NSString )walletAddr\
legalSymbol:(NSString)legalSymbol finish:(void(^)(ICSDKResultModel \\*\
result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
=========== ====== ==== ==============================================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1       
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
=========== ====== ==== ==============================================\
walletAddr  string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
legalSymbol string 
\f0 \'ca\'c7
\f1    
\f0 \'d7\'ca\'b2\'fa\'b5\'c4\'b7\'a8\'b1\'d2\'bc\'c6\'bc\'db\'b5\'a5\'ce\'bb\'a3\'ac\'c8\'cb\'c3\'f1\'b1\'d2\'ce\'aa\'a3\'ba
\f1 CNY
\f0 \'a3\'bb\'c3\'c0\'d4\'aa\'ce\'aa\'a3\'ba
\f1 USD\
=========== ====== ==== ==============================================\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result":[\
           \{\
               "addr":"bcbtestCTLvcA7pa1RqCncL2fRcALgRrVYudJNeE",\
               "coinType":"0x1001",\
               "conAddr":"bcbtestAtEJ4dTejwJReKA4dtFjy9cQ3HzR6jbwF",\
               "name":"BCBT",\
               "symbol":"BCBT",\
               "balance":"101",\
               "last":"2019-04-01T14:21:00.8342387+08:00",\
               "decimals":"9",\
               "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/BCBMainNet.png",\
               "legalValue":"688.8604",\
               "isToken":false,\
               "idx":0,\
               "feeInfo":null\
           \},\
           \{\
               "addr":"bcbtestCTLvcA7pa1RqCncL2fRcALgRrVYudJNeE",\
               "coinType":"0x1001",\
               "conAddr":"bcbtest6e8CEdrcGzX79kRCGJG6h5jVdpdkGDniU",\
               "name":"Diamond Coin",\
               "symbol":"DC",\
               "balance":"0",\
               "last":"2019-04-01T14:21:00.8344546+08:00",\
               "decimals":"9",\
               "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/DC.png",\
               "legalValue":"0",\
               "isToken":true,\
               "idx":2,\
               "feeInfo":null\
           \},\
           \{\
               "addr":"bcbtestCTLvcA7pa1RqCncL2fRcALgRrVYudJNeE",\
               "coinType":"0x1001",\
               "conAddr":"bcbtestHStZsJDbP945H1GbZSJx3xDegtMehMNWK",\
               "name":"USDX",\
               "symbol":"USDX",\
               "balance":"0",\
               "last":"2019-04-01T14:21:00.8344578+08:00",\
               "decimals":"9",\
               "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/USDX.png",\
               "legalValue":"0",\
               "isToken":true,\
               "idx":4,\
               "feeInfo":null\
           \}\
       ]\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ===========================================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ===========================================\
addr       string 
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
coinType   string 
\f0 \'b1\'d2\'d6\'d6\'d6\'f7\'c1\'b4\'b1\'e0\'ba\'c5\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
conAddr    string 
\f0 \'b1\'d2\'d6\'d6\'ba\'cf\'d4\'bc\'b5\'d8\'d6\'b7
\f1 \
name       string 
\f0 \'b1\'d2\'d6\'d6\'c3\'fb\'b3\'c6
\f1 \
symbol     string 
\f0 \'b1\'d2\'d6\'d6\'b4\'fa\'ba\'c5
\f1 \
balance    string 
\f0 \'b5\'d8\'d6\'b7\'b5\'c4\'b4\'cb\'b1\'d2\'d6\'d6\'d3\'e0\'b6\'ee
\f1 \
last       string 
\f0 \'d7\'ee\'ba\'f3\'d2\'bb\'b4\'ce\'b8\'fc\'d0\'c2\'ca\'b1\'bc\'e4
\f1 \
decimals   string 
\f0 \'b1\'d2\'d6\'d6\'be\'ab\'b6\'c8
\f1 \
coinIcon   string 
\f0 \'b1\'d2\'d6\'d6\'cd\'bc\'b1\'ea
\f1 \
legalValue string 
\f0 \'b1\'d2\'d6\'d6\'b5\'c4\'b7\'a8\'b1\'d2\'bc\'db\'d6\'b5
\f1 \
isToken    bool   
\f0 \'ca\'c7\'b7\'f1\'ce\'aa\'b4\'fa\'b1\'d2\'a3\'ac
\f1 true
\f0 \'b1\'ed\'ca\'be\'b4\'fa\'b1\'d2\'a3\'bb
\f1 false
\f0 \'b1\'ed\'ca\'be\'d6\'f7\'c1\'b4\'b1\'be\'b1\'d2
\f1 \
idx        int    
\f0 \'b1\'d2\'d6\'d6\'d4\'da\'c7\'ae\'b0\'fc\'ba\'f3\'cc\'a8\'b5\'c4\'c5\'c5\'d0\'f2\'a3\'ac\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
feeInfo    object 
\f0 \'b1\'d2\'d6\'d6\'b5\'c4\'d7\'aa\'d5\'cb\'ca\'d6\'d0\'f8\'b7\'d1\'c3\'e8\'ca\'f6\'d0\'c5\'cf\'a2
\f1 \
========== ====== ===========================================\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'bb\'f1\'c8\'a1\'d6\'b8\'b6\'a8\'b5\'d8\'d6\'b7\'d7\'ca\'b2\'fa\'b1\'ed\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
4.
\f0 \'bb\'f1\'c8\'a1\'cf\'b5\'cd\'b3\'bf\'c9\'cc\'ed\'bc\'d3\'d7\'ca\'b2\'fa\'c1\'d0\'b1\'ed
\f1 \
------------------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)getAssets:(NSString )walletAddr\
finish:(void(^)(ICSDKResultModel result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ==== ========\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result":[\
           \{\
               "id":4,\
               "cid":2,\
               "coinType":"0x1001",\
               "chainType":1,\
               "chainName":"BCB
\f0 \'c1\'b4
\f1 ",\
               "name":"BCBT",\
               "name_customer":"BCBT",\
               "symbol":"BCBT",\
               "symbol_customer":"BCBT",\
               "decimals":"9",\
               "conAddr":"bcbtestAtEJ4dTejwJReKA4dtFjy9cQ3HzR6jbwF",\
               "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/BCBMainNet.png",\
               "config":1,\
               "idx":0,\
               "appid":"1",\
               "modifyTime":"2018-09-29T13:21:10"\
           \},\
           \{\
               "id":2,\
               "cid":22,\
               "coinType":"0x1001",\
               "chainType":1,\
               "chainName":"BCB
\f0 \'c1\'b4
\f1 ",\
               "name":"Diamond Coin",\
               "name_customer":"Diamond Coin",\
               "symbol":"DC",\
               "symbol_customer":"DC",\
               "decimals":"9",\
               "conAddr":"bcbtest6e8CEdrcGzX79kRCGJG6h5jVdpdkGDniU",\
               "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/DC.png",\
               "config":1,\
               "idx":2,\
               "appid":"1",\
               "modifyTime":"2018-09-27T21:58:30"\
           \},\
           \{\
               "id":6,\
               "cid":21,\
               "coinType":"0x1001",\
               "chainType":1,\
               "chainName":"BCB
\f0 \'c1\'b4
\f1 ",\
               "name":"USDX",\
               "name_customer":"USDX",\
               "symbol":"USDX",\
               "symbol_customer":"USDX",\
               "decimals":"9",\
               "conAddr":"bcbtestHStZsJDbP945H1GbZSJx3xDegtMehMNWK",\
               "coinIcon":"https://testapi.n8.app/public/resource/coin/icon/USDX.png",\
               "config":1,\
               "idx":4,\
               "appid":"1",\
               "modifyTime":"2018-10-30T17:26:02"\
           \}\
       ]\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
=============== ====== ========================================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1           
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
=============== ====== ========================================\
id              int    
\f0 \'d0\'f2\'ba\'c5
\f1 \
cid             int    
\f0 \'ba\'f3\'cc\'a8\'d7\'d6\'b6\'ce\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
coinType        string 
\f0 \'b1\'d2\'d6\'d6\'d6\'f7\'c1\'b4\'b1\'e0\'ba\'c5\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
chainType       int    
\f0 \'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
chainName       string 
\f0 \'c1\'b4\'b5\'c4\'c3\'fb\'b3\'c6\'cb\'b5\'c3\'f7\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
name            string 
\f0 \'b1\'d2\'d6\'d6\'c3\'fb\'b3\'c6
\f1 \
name_customer   string 
\f0 \'bf\'cd\'bb\'a7\'d7\'d4\'b6\'a8\'d2\'e5\'b5\'c4\'b1\'d2\'d6\'d6\'c3\'fb\'b3\'c6\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
symbol          string 
\f0 \'b1\'d2\'d6\'d6\'b7\'fb\'ba\'c5
\f1 \
symbol_customer string 
\f0 \'bf\'cd\'bb\'a7\'d7\'d4\'b6\'a8\'d2\'e5\'b5\'c4\'b1\'d2\'d6\'d6\'b7\'fb\'ba\'c5\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
decimals        string 
\f0 \'b1\'d2\'d6\'d6\'d0\'a1\'ca\'fd\'b5\'e3\'be\'ab\'b6\'c8
\f1 \
conAddr         string 
\f0 \'b1\'d2\'d6\'d6\'ba\'cf\'d4\'bc\'b5\'d8\'d6\'b7
\f1 \
coinIcon        string 
\f0 \'b1\'d2\'d6\'d6
\f1 logo
\f0 \'b5\'c4\'b5\'d8\'d6\'b7
\f1 \
config          int    
\f0 \'b1\'d2\'d6\'d6\'ca\'c7\'b7\'f1\'bf\'c9\'d2\'d4\'c5\'e4\'d6\'c3\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
idx             int    
\f0 \'b1\'d2\'d6\'d6\'b5\'c4\'d7\'d4\'b6\'a8\'d2\'e5\'c5\'c5\'d0\'f2\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
appid           int    
\f0 \'d3\'a6\'d3\'c3
\f1 id
\f0 \'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
modifyTime      string 
\f0 \'d7\'ee\'ba\'f3\'d2\'bb\'b4\'ce\'b8\'fc\'d0\'c2\'ca\'b1\'bc\'e4
\f1 \
=============== ====== ========================================\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'b2\'e9\'d1\'af\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
5.
\f0 \'b2\'e9\'d1\'af\'d6\'b8\'b6\'a8\'b5\'d8\'d6\'b7\'a1\'a2\'d6\'b8\'b6\'a8\'b1\'d2\'d6\'d6\'d0\'c5\'cf\'a2
\f1 \
----------------------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)getCoinDeatil:(NSString )walletAddr coinAddr:(NSString)coinAddr\
legalSymbol:(NSString )legalSymbol finish:(void(^)(ICSDKResultModel\
result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
=========== ====== ==== ==================================================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1       
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
=========== ====== ==== ==================================================\
walletAddr  string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
conAddr     string 
\f0 \'ca\'c7
\f1    
\f0 \'b1\'d2\'d6\'d6\'ba\'cf\'d4\'bc\'b5\'d8\'d6\'b7
\f1 \
legalSymbol string 
\f0 \'ca\'c7
\f1    
\f0 \'b1\'d2\'d6\'d6\'d7\'ca\'b2\'fa\'b5\'c4\'b7\'a8\'b1\'d2\'bc\'c6\'bc\'db\'b5\'a5\'ce\'bb\'a3\'ac\'c8\'cb\'c3\'f1\'b1\'d2\'ce\'aa\'a3\'ba
\f1 CNY
\f0 \'a3\'bb\'c3\'c0\'d4\'aa\'ce\'aa\'a3\'ba
\f1 USD\
=========== ====== ==== ==================================================\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result":\{\
           "addr":"bcbESMNFs8Cekc9H6xQcu3a2p4NvJDtNoy8S",\
           "coinType":"0x1002",\
           "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",\
           "name":"BCB",\
           "symbol":"BCB",\
           "balance":"4.99905",\
           "last":"2019-04-01T14:44:20.4735693+08:00",\
           "decimals":"9",\
           "coinIcon":"https://www.n8.app/public/resource/coin/icon/BCBMainNet.png",\
           "legalValue":"215.21092615344",\
           "isToken":false,\
           "idx":65535,\
           "feeInfo":\{\
               "id":1,\
               "isUniteCoin":false,\
               "conAddr":"bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",\
               "percent":0,\
               "maxfee":null,\
               "minfee":null,\
               "feeName":null,\
               "bcbFee":"0.00125",\
               "modifyTime":"2018-11-01T08:56:40"\
           \}\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ================================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ================================\
addr       string 
\f0 \'b5\'d8\'d6\'b7
\f1 \
coinType   string 
\f0 \'b1\'d2\'d6\'d6\'d6\'f7\'c1\'b4\'b1\'e0\'ba\'c5\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
conAddr    string 
\f0 \'b1\'d2\'d6\'d6\'ba\'cf\'d4\'bc\'b5\'d8\'d6\'b7
\f1 \
name       string 
\f0 \'b1\'d2\'d6\'d6\'c3\'fb\'b3\'c6
\f1 \
symbol     string 
\f0 \'b1\'d2\'d6\'d6\'b7\'fb\'ba\'c5
\f1 \
balance    string 
\f0 \'b5\'d8\'d6\'b7\'b5\'c4\'b4\'cb\'b1\'d2\'d6\'d6\'d3\'e0\'b6\'ee
\f1 \
last       string 
\f0 \'d7\'ee\'ba\'f3\'d2\'bb\'b4\'ce\'b8\'fc\'d0\'c2\'ca\'b1\'bc\'e4
\f1 \
decimals   string 
\f0 \'b1\'d2\'d6\'d6\'d0\'a1\'ca\'fd\'b5\'e3\'be\'ab\'b6\'c8
\f1 \
coinIcon   string 
\f0 \'b1\'d2\'d6\'d6
\f1 logo
\f0 \'b5\'c4\'b5\'d8\'d6\'b7
\f1 \
legalValue string 
\f0 \'b1\'d2\'d6\'d6\'b5\'c4\'b7\'a8\'b1\'d2\'bc\'db\'d6\'b5
\f1 \
isToken    bool   
\f0 \'ca\'c7\'b7\'f1\'ce\'aa\'b4\'fa\'b1\'d2
\f1 \
idx        int    
\f0 \'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
feeInfo    object 
\f0 \'b1\'d2\'d6\'d6\'ca\'d6\'d0\'f8\'b7\'d1\'c3\'e8\'ca\'f6\'d0\'c5\'cf\'a2
\f1 \
========== ====== ================================\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'b2\'e9\'d1\'af\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
6.
\f0 \'b2\'e9\'d1\'af\'d6\'b8\'b6\'a8\'b1\'d2\'d6\'d6\'bd\'bb\'d2\'d7\'bc\'c7\'c2\'bc
\f1 \
----------------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(void)getCoinTransactionDetail:(NSString )walletAddr\
conAddr:(NSString)coinAddr page:(NSInteger)page count:(NSInteger)count\
finish:(void(^)(ICSDKResultModel \\* result))finish;**\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ============\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ============\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
conAddr    string 
\f0 \'ca\'c7
\f1    
\f0 \'b1\'d2\'d6\'d6\'ba\'cf\'d4\'bc\'b5\'d8\'d6\'b7
\f1 \
page       int    
\f0 \'ca\'c7
\f1    
\f0 \'d2\'b3\'c2\'eb\'b4\'d3
\f1 0
\f0 \'bf\'aa\'ca\'bc
\f1 \
count      int    
\f0 \'ca\'c7
\f1    
\f0 \'cc\'f5\'ca\'fd
\f1 \
========== ====== ==== ============\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result":\{\
           "records":[\
               \{\
                   "id":12858549,\
                   "coinType":"0x1002",\
                   "from":"bcb2kerqmq8ZRPneB4mp2Qv4qSwDyhtLYwb8",\
                   "to":"bcbESMNFs8Cekc9H6xQcu3a2p4NvJDtNoy8S",\
                   "conAddr":"bcbCsRXXMGkUJ8wRnrBUD7mQsMST4d53JRKJ",\
                   "value":"175.756694",\
                   "valueName":"DC",\
                   "fee":"0.0015",\
                   "feeName":"BCB",\
                   "timeStamp":"1553238936",\
                   "blockN":"9603760",\
                   "source":null,\
                   "txHash":"D67097C9E342213B7F46C8D680C96099907A81096E975847D7C204CDA76CAD70",\
                   "memo":"BalancePo CoinTransfer:1553238925228RK7EwEBSC1KO",\
                   "status":"0x1",\
                   "balanceFromFlag":0,\
                   "balanceToFlag":0,\
                   "pushFromCnt":0,\
                   "modifyTime":"2019-03-22T15:15:37"\
               \}\
           ]\
       \} \
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
=============== ====== ================================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1           
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
=============== ====== ================================\
id              int    
\f0 \'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
coinType        string 
\f0 \'b1\'d2\'d6\'d6\'d6\'f7\'c1\'b4\'b1\'e0\'ba\'c5\'a3\'ac\'b5\'da\'c8\'fd\'b7\'bd\'d3\'a6\'d3\'c3\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
from            string 
\f0 \'d7\'aa\'b3\'f6\'b7\'bd\'b5\'d8\'d6\'b7
\f1 \
to              string 
\f0 \'ca\'d5\'bf\'ee\'c8\'cb\'b5\'d8\'d6\'b7
\f1 \
conAddr         string 
\f0 \'b1\'d2\'d6\'d6\'ba\'cf\'d4\'bc\'b5\'d8\'d6\'b7
\f1 \
value           string 
\f0 \'d7\'aa\'d5\'cb\'bd\'f0\'b6\'ee
\f1 \
valueName       string 
\f0 \'d7\'aa\'d5\'cb\'bd\'f0\'b6\'ee\'c3\'fb\'b3\'c6
\f1 \
fee             string 
\f0 \'ca\'d6\'d0\'f8\'b7\'d1\'bd\'f0\'b6\'ee\'b7\'dd\'b6\'ee
\f1 \
feeName         string 
\f0 \'ca\'d6\'d0\'f8\'b7\'d1\'b1\'d2\'d6\'d6\'c3\'fb\'b3\'c6
\f1 \
timeStamp       string 
\f0 \'d7\'aa\'d5\'cb\'ca\'b1\'bc\'e4\'b4\'c1
\f1 \
blockN          string 
\f0 \'c7\'f8\'bf\'e9\'ba\'c5
\f1 \
source                 
\f0 \'b5\'da\'c8\'fd\'b7\'bd\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
txHash          string 
\f0 \'bd\'bb\'d2\'d7
\f1 hash\
memo            string 
\f0 \'bd\'bb\'d2\'d7\'b1\'b8\'d7\'a2\'d0\'c5\'cf\'a2
\f1 \
status          string 
\f0 \'bd\'bb\'d2\'d7\'ca\'c7\'b7\'f1\'b3\'c9\'b9\'a6\'a3\'ac
\f1 \'930x1\'94
\f0 \'b1\'ed\'ca\'be\'b3\'c9\'b9\'a6
\f1 \
balanceFromFlag int    
\f0 \'b5\'da\'c8\'fd\'b7\'bd\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
balanceToFlag   int    
\f0 \'b5\'da\'c8\'fd\'b7\'bd\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
pushFromCnt     int    
\f0 \'b5\'da\'c8\'fd\'b7\'bd\'ce\'de\'d0\'e8\'b9\'d8\'d0\'c4
\f1 \
modifyTime      string 
\f0 \'d7\'ee\'ba\'f3\'d2\'bb\'b4\'ce\'d0\'de\'b8\'c4\'ca\'b1\'bc\'e4
\f1 \
=============== ====== ================================\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'b2\'e9\'d1\'af\'ca\'a7\'b0\'dc
\f1 ",\
       "result":\{\}\
   \}\
\
4.OTC
\f0 \'bc\'b0\'c9\'c1\'b6\'d2\'c4\'a3\'bf\'e9
\f1 \
===============\
\
1.OTC
\f0 \'c4\'a3\'bf\'e9\'c6\'a4\'b7\'f4\'d6\'f7\'cc\'e2\'c9\'e8\'d6\'c3
\f1 \
---------------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
-(**void**)setOtcTheme:(ICOTCThemeType)theme;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
====== ==== ==== ========================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1  
\f0 \'c0\'e0\'d0\'cd
\f1  
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
====== ==== ==== ========================\
theme  int  
\f0 \'ca\'c7
\f1    0
\f0 \'a3\'ba\'b0\'d7\'c9\'ab\'d6\'f7\'cc\'e2\'a1\'a2
\f1 1
\f0 \'a3\'ba\'b0\'b5\'c9\'ab\'d6\'f7\'cc\'e2
\f1 \
====== ==== ==== ========================\
\
2.OTC
\f0 \'c8\'eb\'bf\'da
\f1 \
---------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**[[OTCStart manager] OTCStart];**\
\
3.OTC
\f0 \'c2\'f2\'b1\'d2\'c7\'bf\'d6\'c6\'b0\'f3\'b6\'a8\'d2\'f8\'d0\'d0\'bf\'a8\'c9\'e8\'d6\'c3
\f1 \
---------------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -2:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
-(**void**)setOtcBuyBindBankCard:(\\ **BOOL**)bind;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
====== ==== ==== =========================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1  
\f0 \'c0\'e0\'d0\'cd
\f1  
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
====== ==== ==== =========================\
bind   Bool 
\f0 \'ca\'c7
\f1    
\f0 \'c4\'ac\'c8\'cf\'b2\'bb\'c7\'bf\'d6\'c6\'a3\'ac\'c7\'bf\'d6\'c6\'b0\'f3\'b6\'a8\'ce\'aa
\f1 YES\
====== ==== ==== =========================\
\
4.
\f0 \'c9\'c1\'b6\'d2\'c8\'eb\'bf\'da
\f1 \
----------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -3:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**[[OTCStart manager] fastexStart];**\
\
5.
\f0 \'b9\'a4\'be\'df
\f1 \
======\
\
1.
\f0 \'ca\'c7\'b7\'f1\'ce\'aa
\f1 BYB
\f0 \'b9\'c9\'b6\'ab
\f1 \
---------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -4:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(**\\ void**)bybJudgeHolder:(NSString *)walletAddr\
finish:(\\ *\\ **void**\\ *\\ (^)(ICSDKResultModel* result))finish;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ==== ========\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{   \
           "holder":"0",\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
====== ====== ==================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1  
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
====== ====== ==================\
holder string 0
\f0 \'a3\'ba\'b7\'c7\'b9\'c9\'b6\'ab\'a3\'ac
\f1 1
\f0 \'a3\'ba\'b9\'c9\'b6\'ab
\f1 \
====== ====== ==================\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'cd\'f8\'c2\'e7\'b4\'ed\'ce\'f3
\f1 ",\
       "result":\{\}\
   \}\
\
2.
\f0 \'bb\'f1\'c8\'a1
\f1 BYB
\f0 \'c8\'be\'c9\'ab\'cc\'e5
\f1 \
---------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(**\\ void**)bybBalanceItems:(NSString *)walletAddr\
finish:(\\ *\\ **void**\\ *\\ (^)(ICSDKResultModel* result))finish;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ========\
walletAddr string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
========== ====== ==== ========\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": \
       \{   \
           "chromo":"2",\
           "balance":"100",\
       \}\
   \}\
\
**
\f0 \'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
======= ====== ==========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1   
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'cb\'b5\'c3\'f7
\f1 \
======= ====== ==========\
chromo  string 
\f0 \'c8\'be\'c9\'ab\'cc\'e5\'ba\'c5\'c2\'eb
\f1 \
balance string 
\f0 \'c8\'be\'c9\'ab\'cc\'e5\'d3\'e0\'b6\'ee
\f1 \
======= ====== ==========\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1001,\
       "msg": "
\f0 \'cd\'f8\'c2\'e7\'b4\'ed\'ce\'f3
\f1 ",\
       "result":\{\}\
   \}\
\
3.
\f0 \'bc\'d3\'c3\'dc
\f1 \
------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(**\\ void**)encryptContent:(NSString *)content\
finish:(\\ *\\ **void**\\ *\\ (^)(ICSDKResultModel* result))finish;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
======= ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1   
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
======= ====== ==== ========\
content string 
\f0 \'ca\'c7
\f1    
\f0 \'bc\'d3\'c3\'dc\'c4\'da\'c8\'dd
\f1 \
======= ====== ==== ========\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -1:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": "/suzXLeVk3tU3AmFe1/lhA=="\
   \}\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1,\
       "msg": "fail",\
       "result":""\
   \}\
\
4.
\f0 \'bd\'e2\'c3\'dc
\f1 \
------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -2:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(**\\ void**)decryptContent:(NSString *)content\
finish:(\\ *\\ **void**\\ *\\ (^)(ICSDKResultModel* result))finish;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
======= ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1   
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
======= ====== ==== ========\
content string 
\f0 \'ca\'c7
\f1    
\f0 \'bd\'e2\'c3\'dc\'c4\'da\'c8\'dd
\f1 \
======= ====== ==== ========\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -2:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "ok",\
       "result": "123"\
   \}\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1,\
       "msg": "fail",\
       "result":""\
   \}\
\
5.
\f0 \'ca\'fd\'be\'dd\'d1\'e9\'c7\'a9
\f1 \
----------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(**\\ void\\ **)verifySign:(NSString )type data:(NSString)data\
pubKey:(NSString )pubKey signature:(NSString)signature\
finish:(**\\ void**(^)(ICSDKResultModel \\* result))finish;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========= ====== ==== =======================\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1     
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========= ====== ==== =======================\
type      string 
\f0 \'ca\'c7
\f1    
\f0 \'cb\'e3\'b7\'a8
\f1 \
data      string 
\f0 \'ca\'c7
\f1    
\f0 \'b4\'fd\'d1\'e9\'c7\'a9\'c4\'da\'c8\'dd\'a3\'a8
\f1 hexstring
\f0 \'a3\'a9
\f1 \
pubKey    string 
\f0 \'ca\'c7
\f1    
\f0 \'d1\'e9\'c7\'a9\'b9\'ab\'d4\'bf\'a3\'a8
\f1 hexstring
\f0 \'a3\'a9
\f1 \
signature string 
\f0 \'ca\'c7
\f1    
\f0 \'c7\'a9\'c3\'fb\'a3\'a8
\f1 hexstring
\f0 \'a3\'a9
\f1 \
========= ====== ==== =======================\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "success",\
       "result": ""\
   \}\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1,\
       "msg": "verify fail",\
       "result":""\
   \}\
\
6.
\f0 \'b8\'f9\'be\'dd\'d6\'fa\'bc\'c7\'b4\'ca\'b7\'b5\'bb\'d8\'b6\'d4\'d3\'a6\'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
----------------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -1:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(**\\ void**)getAddrFromMnemonicWords:(NSString *)mnemonicWords\
finish:(\\ *\\ **void**\\ *\\ (^)(ICSDKResultModel* result))finish;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
============= ====== ==== ======\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1         
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
============= ====== ==== ======\
mnemonicWords string 
\f0 \'ca\'c7
\f1    
\f0 \'d6\'fa\'bc\'c7\'b4\'ca
\f1 \
============= ====== ==== ======\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -1:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "",\
       "result": \{\
           "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"\
       \}\
   \}\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1,\
       "msg": "fail",\
       "result":""\
   \}\
\
7.
\f0 \'b8\'f9\'be\'dd\'cb\'bd\'d4\'bf\'b7\'b5\'bb\'d8\'b6\'d4\'d3\'a6\'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
--------------------------\
\
.. _
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 -2:\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(**\\ void**)getAddrFromPrivateKey:(NSString *)privateKey\
finish:(\\ *\\ **void**\\ *\\ (^)(ICSDKResultModel* result))finish;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
========== ====== ==== ====\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1      
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
========== ====== ==== ====\
privateKey string 
\f0 \'ca\'c7
\f1    
\f0 \'cb\'bd\'d4\'bf
\f1 \
========== ====== ==== ====\
\
.. _
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -2:\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "",\
       "result": \{\
           "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"\
       \}\
   \}\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1,\
       "msg": "fail",\
       "result":""\
   \}\
\
8.
\f0 \'b8\'f9\'be\'dd
\f1 Keystore
\f0 \'b7\'b5\'bb\'d8\'b6\'d4\'d3\'a6\'c7\'ae\'b0\'fc\'b5\'d8\'d6\'b7
\f1 \
------------------------------\
\
1.1 
\f0 \'b7\'bd\'b7\'a8\'d4\'ad\'d0\'cd
\f1 \
~~~~~~~~~~~~\
\
**-(**\\ void\\ **)getAddrFromKeystore:(NSString )keystore\
password:(NSString)password finish:(**\\ void**(^)(ICSDKResultModel \\*\
result))finish;\
\
**
\f0 \'b2\'ce\'ca\'fd\'d7\'d6\'b6\'ce\'cb\'b5\'c3\'f7
\f1 **\
\
======== ====== ==== ========\

\f0 \'d7\'d6\'b6\'ce\'c3\'fb
\f1    
\f0 \'c0\'e0\'d0\'cd
\f1    
\f0 \'b1\'d8\'d0\'eb
\f1  
\f0 \'cb\'b5\'c3\'f7
\f1 \
======== ====== ==== ========\
keystore string 
\f0 \'ca\'c7
\f1    keystore\
password string 
\f0 \'ca\'c7
\f1    
\f0 \'c3\'dc\'c2\'eb
\f1 \
======== ====== ==== ========\
\
1.2 
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 \
~~~~~~~~~~~~\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'d5\'fd\'c8\'b7\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":0,\
       "msg": "",\
       "result": \{\
           "walletAddr":"bcbNg7srN9byDMLGL6tG18WEMFLExpVQqGX5"\
       \}\
   \}\
\
**
\f0 \'b7\'b5\'bb\'d8\'bd\'e1\'b9\'fb
\f1 -
\f0 \'b4\'ed\'ce\'f3\'ca\'b1
\f1 **\
\
.. code:: java\
\
   \{\
       "code":-1,\
       "msg": "fail",\
       "result":""\
   \}\
}