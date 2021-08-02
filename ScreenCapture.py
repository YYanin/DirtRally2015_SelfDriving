#

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui



def process_img(original_image):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
	return processed_img

# #Timer to unpause the game
# for i in list(range(4))[::-1]:
# 	print(i+1)
# 	time.sleep(1)





last_time = time.time()
while(True):
	screen =  np.array(ImageGrab.grab(bbox=(0,40,1024,768)))

	#Test run for key input
	print('down')
	pyautogui.keyDown('w')
	time.sleep(3)
	print('up')
	pyautogui.keyUp('w')


	new_screen = process_img(screen)


	cv2.imshow('window', new_screen)
	#cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break


	print('Loop took {} seconds' .format(time.time()-last_time))
	last_time=time.time()




##############################################################
# import sys 

# print(sys.executable)

