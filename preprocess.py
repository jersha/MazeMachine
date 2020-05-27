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
sizeBV = 0
sizeBH = 0
selectedrows = np.array([], dtype = np.int64)
selectedcolumns = np.array([], dtype = np.int64)
shortlistedrows = np.array([], dtype = np.int64)
shortlistedcolumns = np.array([], dtype = np.int64)
finalimage = np.array([], dtype = np.int64)

blackwhite_image = BlackWhite(image)
top_border, bottom_border, left_border, right_border = FindBorder(blackwhite_image)
if(top_border == -1 or bottom_border == -1 or left_border == -1 or right_border == -1):
    print('Error:Not able to find the border')
    exit()

sizeBV, sizeBH = FindSizeB(blackwhite_image, top_border, bottom_border, left_border, right_border)
sizeBV_half = sizeBV // 2
sizeBH_half = sizeBH // 2

if(sizeBV == -1 or sizeBH == -1):
    print('Error:Not able to find the size of Black')
    exit()

top_borderin = top_border + sizeBV
bottom_borderin = bottom_border - sizeBV
left_borderin = left_border + sizeBH
right_borderin = right_border - sizeBH
selectedrows = RowsSelect(blackwhite_image, top_borderin, bottom_borderin, 
                          left_borderin, right_borderin, sizeBH)
selectedcolumns = ColumnssSelect(blackwhite_image, top_borderin, bottom_borderin, 
                                 left_borderin, right_borderin, sizeBV)
shortlistedrows = ShortlistedRows(selectedrows, sizeBV_half, top_border, top_borderin, bottom_border, bottom_borderin)
shortlistedcolumns = ShortlistedColumns(selectedcolumns, sizeBH_half, left_border, left_borderin, right_border, right_borderin)

finalimage = CreateImage(blackwhite_image, shortlistedrows, shortlistedcolumns)
cv2.imwrite('output.png', np.asarray(finalimage))













