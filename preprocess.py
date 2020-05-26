import cv2
import numpy as np
from preprocess_fun import *
        
image = cv2.imread('maze.jpg')
cv2.imwrite('image.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
image = cv2.imread('image.jpg')
top_border = 0
bottom_border = 0
left_border = 0
right_border = 0
sizeB = 0
sizeW = 0

blackwhite_image = BlackWhite(image)
top_border, bottom_border, left_border, right_border = FindLB(blackwhite_image)
if(top_border == -1 or bottom_border == -1 or left_border == -1 or right_border == -1):
    print('Error:Not able to find the border')
    exit()
else:
    print('top_border = ', top_border,'\n',
          'bottom_border = ', bottom_border,'\n',
          'left_border = ', left_border,'\n',
          'right_border = ', right_border)

sizeB = FindSizeB(blackwhite_image, top_border)
if(sizeB == -1):
    print('Error:Not able to find the size of Black')
    exit()
else:
    print('SizeBlack = ', sizeB)
    
sizeW = FindSizeW(blackwhite_image, top_border)
if(sizeW == -1):
    print('Error:Not able to find the size of White')
    exit()
else:
    print('SizeWhite = ', sizeW,'\n')
    
horizontalstart = left_border + (sizeB // 2)
verticalstart = top_border + (sizeB // 2)

temp_buffer = np.array([])
image_buffer = np.array([])
horizontalposition = horizontalstart
verticalposition = verticalstart
first = 1
while verticalposition < bottom_border:
    while horizontalposition < right_border:
        temp_buffer = np.hstack((temp_buffer, np.array(blackwhite_image[verticalposition][horizontalposition])))
        horizontalposition += sizeB
    if(first == 1):
        image_buffer = np.hstack((image_buffer, temp_buffer))
        first = 0
    else:
        image_buffer = np.vstack((image_buffer, temp_buffer))
    temp_buffer = np.array([])
    horizontalposition = horizontalstart
    verticalposition += sizeB

cv2.imwrite('output.png', np.asarray(image_buffer))
    
