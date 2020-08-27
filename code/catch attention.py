import bluetooth
import numpy as np
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
with open("Output.txt", "w") as text_file: #輸出資料
	if __name__=='__main__':
		mindwaveDataPointReader = MindwaveDataPointReader(address='98:07:2D:7F:40:FF') #輸入你的腦波儀序號
		mindwaveDataPointReader.start() 
		if (mindwaveDataPointReader.isConnected()):
			while(True):
				dataPoint = mindwaveDataPointReader.readNextDataPoint()
				if ( dataPoint.__class__.__name__ == 'AttentionDataPoint'):
					x=np.array(dataPoint)
					print(dataPoint)
					print(f"{dataPoint}", file=text_file)			
			else:
				pass
		else:
			print('Exiting because the program could not connect to the TGAM device.')


	
