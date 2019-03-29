import numpy as np
import time
from os import system
import glob
import os
import quikeval_runner as qr

# logfile (format = LTC2344_18_log_##.txt)
filename_form = "C:\\Users\\User\\Documents\\LTC2344_18_log_"
extension = ".txt"
	

#create a list for each channel 
ch0_list = []
ch1_list = []
ch2_list = []
ch3_list = []

for i in range(2000):
	
	qr.logFile()
	system('cls')
	#filename = filename_form + str(i) + extension #reconstruct filename
	# choose starting log file number (check the latest log file)
	list_of_files = glob.glob('C:\\Users\\User\\Documents\\*.txt') # * means all if need specific format then *.csv
	latest_file = max(list_of_files, key=os.path.getctime)
	#print(latest_file)
	with open(latest_file) as file: #open file
		lines = file.readlines()	
		
	# take away the first 14 lines
	data = lines[14:]	
	
	for line in data: #lines from raw data
		if len(line) > 1:
			channel1,channel2,channel3,channel4 = line.split(',') #split channels
			channel4 = channel4[:-1] #take off '/n' for 4th channel
			ch0_list.append(float(channel1)) #add value to channel 1 list
			ch1_list.append(float(channel2)) #add value to channel 2 list
			ch2_list.append(float(channel3)) #add value to channel 3 list		
			ch3_list.append(float(channel4)) #add value to channel 4 list

	ch0 = np.asarray(ch0_list)
	ch1 = np.asarray(ch1_list)
	ch2 = np.asarray(ch2_list)
	ch3 = np.asarray(ch3_list)

	ch0_av = np.average(ch0) #returns the average of array
	ch1_av = np.average(ch1)
	ch2_av = np.average(ch2)
	ch3_av = np.average(ch3)
		
	# Voltage function for HR=25%
	ch0_Voltage25 = (ch0_av * 0.000015589159323 + 2.060889674577856)
	ch1_Voltage25 = (ch1_av * 0.000015589159323 + 2.060889674577856)
	ch2_Voltage25 = (ch2_av * 0.000015589159323 + 2.060889674577856)
	ch3_Voltage25 = (ch3_av * 0.000015589159323 + 2.060889674577856)

	# Voltage function for HR=50%
	ch0_Voltage50 = (ch0_av * 0.000015547260802 + 2.055655404021672)
	ch1_Voltage50 = (ch1_av * 0.000015547260802 + 2.055655404021672)
	ch2_Voltage50 = (ch2_av * 0.000015547260802 + 2.055655404021672)
	ch3_Voltage50 = (ch3_av * 0.000015547260802 + 2.055655404021672)


	# Voltage function for HR=65%
	ch0_Voltage65 = (ch0_av * 0.000015547849903 + 2.055988525529228)
	ch1_Voltage65 = (ch1_av * 0.000015547849903 + 2.055988525529228)
	ch2_Voltage65 = (ch2_av * 0.000015547849903 + 2.055988525529228)
	ch3_Voltage65 = (ch3_av * 0.000015547849903 + 2.055988525529228)




	# Humidity function 
	Cof1= -0.0000000000001472129234750049
	Cof2= -0.00000002777775067690840
	Cof3= -0.001965680219868
	Cof4= -61.825175871201033
	Cof5= -729150.7220528035

#print(Cof1)

	#ch3_Humidity = Cof1 * ch3_av ** 4 + Cof2 * ch3_av ** 3 + Cof3 * ch3_av ** 2 + Cof4 * ch3_av ** 1 + Cof5
	
	ch0_Humidity = Cof1 * (ch0_av ** 4)  + Cof2 * (ch0_av ** 3) + Cof3 * (ch0_av ** 2) + Cof4 * (ch0_av ** 1) + Cof5
	ch1_Humidity = Cof1 * (ch1_av ** 4)  + Cof2 * (ch1_av ** 3) + Cof3 * (ch1_av ** 2) + Cof4 * (ch1_av ** 1) + Cof5
	ch2_Humidity = Cof1 * (ch2_av ** 4)  + Cof2 * (ch2_av ** 3) + Cof3 * (ch2_av ** 2) + Cof4 * (ch2_av ** 1) + Cof5
	ch3_Humidity = Cof1 * (ch3_av ** 4)  + Cof2 * (ch3_av ** 3) + Cof3 * (ch3_av ** 2) + Cof4 * (ch3_av ** 1) + Cof5

	#ch1_Humidity = -0.0000000000001472129234750049 * (ch1_av ** 4)  - 0.00000002777775067690840 * (ch1_av ** 3) - 0.001965680219868 * (ch1_av ** 2) - 61.825175871201033 * (ch1_av ** 1) - 729150.7220528035
	#ch2_Humidity = -0.0000000000001472129234750049 * (ch2_av ** 4)  - 0.00000002777775067690840 * (ch2_av ** 3) - 0.001965680219868 * (ch2_av ** 2) - 61.825175871201033 * (ch2_av ** 1) - 729150.7220528035
	#ch3_Humidity = -0.0000000000001472129234750049 * (ch3_av ** 4)  - 0.00000002777775067690840 * (ch3_av ** 3) - 0.001965680219868 * (ch3_av ** 2) - 61.825175871201033 * (ch3_av ** 1) - 729150.7220528035
	
	
	#print Average Channel Digital Values 
	print("\n Average Digital Values (channel 0 to 3): ")
	print(ch0_av)
	print(ch1_av)
	print(ch2_av)
	print(ch3_av)

	#print Voltages for channels
	#print("\n Voltages Values (channel 0 to 3): ")
	#print(ch0_Voltage)
	#print(ch1_Voltage)
	#print(ch2_Voltage)
	#print(ch3_Voltage)


	#print Humidity for channels
	print("\n Humidity Values (channel 0 to 3): ")
	print(ch0_Humidity)
	print(ch1_Humidity)
	print(ch2_Humidity)
	print(ch3_Humidity)

	ch0_list = []
	ch1_list = []
	ch2_list = []
	ch3_list = []
	
	#Delete file
	os.remove(latest_file)

