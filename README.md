# MindWave-Mobile-catch-attention-
* 使用Neurosky所研發，MindWave Mobile 2中的Mindwave Starter Kit
* 使用ubuntu中的python3執行程式

## mindwavemobile程式碼來源
from  [https://github.com/robintibor](https://github.com/robintibor/python-mindwave-mobile)

## 環境安裝
* 藍芽
> sudo apt-get install libbluetooth-dev python-bluetooth
* 將mindwavemobile下載為函式庫
> python setup.py install

## 程式介紹

  * import:
  > import bluetooth
  
  > import numpy as np
  
  > from mindwavemobile.MindwaveDataPoints import RawDataPoint
  
  > from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
  
  * 腦波儀序號:
  > mindwaveDataPointReader = MindwaveDataPointReader(address='98:07:2D:7F:40:FF') #輸入你的腦波儀序號
  
     > 腦波儀序號由藍芽連接介面的該儀器詳細介紹可找到
     
## 補充
   若想擷取其他腦波儀資訊，可將以下'AttentionDataPoint'替換
   
   > if ( dataPoint.__class__.__name__ == 'AttentionDataPoint'):

## 腦波儀可能連接問題
* Ubuntu bluetooth無法連接
  > mindwave只可連接1個裝置(電腦)，請檢查是否有其他藍芽誤連
* 訊號異常
  > 將藍芽取消連接，重新配對
  > 注意裝置是否佩戴正確(額前須貼齊)
* 程式無法執行
  > 注意python版本，有的terminal必須輸入'python3 XX.py'
