#

import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()

while(True):
    screen =  np.array(ImageGrab.grab(bbox=(0,40,1024,768)))
    #printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')


    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


    print('Loop took {} seconds' .format(time.time()-last_time))
    last_time=time.time()
# print('Hello World!')