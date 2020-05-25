import numpy as np
import cv2

x_train = np.empty((21, 21), dtype='float16')
for i in range(900, 1000):
    x_train = cv2.imread('mazes/out_test/output{}.png'.format(i), 0)  
    x_train[x_train == 0] = 255              
    x_train[x_train == 147] = 0               
    cv2.imwrite('mazes/lol/output%d.png' %(i), x_train)