import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import time


# logfile (format = LTC2344_18_log_##.txt)
filename_form = "C:\\Users\\User\\Documents\\LTC2344_18_log_"
extension = ".txt"

# choose ##
start = 55
stop = 56

def genSec(i): #generates 40 deciseconds
	y = range(1*i,41*i)
	z = np.array(y)/10
	return z
	
 #interactive mode
fig = plt.figure() #generate empty figure
ax = fig.add_subplot(1,1,1)

#create a list for each channel 
channel1_list = []
channel2_list = []
channel3_list = []
channel4_list = []


seconds = np.array([])
def extractDatatoLists(start, stop):
	for i in range (start,stop): #for each number from start to stop 
		filename = filename_form + str(i) + extension #reconstruct filename
		
		with open(filename) as file: #open file
			lines = file.readlines()	
			
		# take away the first 14 lines
		data = lines[14:]	
		
		for line in data: #lines from raw data
			if len(line) > 1:
				channel1,channel2,channel3,channel4 = line.split(',') #split channels
				channel4 = channel4[:-1] #take off ',' for 4th channel
				channel1_list.append(float(channel1)) #add value to channel 1 list
				channel2_list.append(float(channel2)) #add value to channel 2 list
				channel3_list.append(float(channel3)) #add value to channel 3 list
				channel4_list.append(float(channel4)) #add value to channel 4 list
				
		ax.clear()
		ax.plot(genSec(1), np.array(channel1_list))

ani = animation.FuncAnimation(fig, extractDatatoLists(start,stop), interval=4000)

plt.show()
print(channel1_list)
