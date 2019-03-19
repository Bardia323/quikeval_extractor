import pyautogui as pg
import time
#open quikeval shortcut
	

	#ok_button position : 

	#doubleClick Icon @ (42, 752)
#pg.doubleClick(42,752)
	#wait until program launches
#time.sleep(5)
#start loop	
def getpos(image):
	x, y = pg.locateCenterOnScreen(image, confidence=0.9)
	return x, y
	


for i in range(0, 10):
	try:
		#click "log" @ log_pos
		log_pos = getpos('log.png')
		pg.click(log_pos)
	except TypeError:
		log_white_pos = getpos('log_white.png')
		pg.click(log_white_pos)
	
	time.sleep(0.3)
	#click start logging
	try:
		start_log_pos = getpos('Start_logging.png')
		pg.click(start_log_pos)
	except TypeError:
		time.sleep(0.2)
		start_log_pos = getpos('Start_logging.png')
		pg.click(start_log_pos)
	# wait 4 seconds
	time.sleep(4.7)
	#click ok button @ (850, 500)
	try:
		ok_pos = getpos('OK.png')
		pg.click(ok_pos)
	except TypeError:
		time.sleep(1)
		ok_pos = getpos('OK.png')
		pg.click(ok_pos)
	
	
#end loop
