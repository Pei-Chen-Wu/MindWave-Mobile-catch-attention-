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
     
