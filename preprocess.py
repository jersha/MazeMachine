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

shortlistedrows = np.hstack((shortlistedrows, np.array(top_border + sizeBV_half)))
shortlistedrows = np.hstack((shortlistedrows, np.array(top_borderin + sizeBV_half)))
shortlistedrows_temp = ShortlistedRows(selectedrows, sizeBH)
shortlistedrows = np.hstack((shortlistedrows, shortlistedrows_temp))
shortlistedrows = np.hstack((shortlistedrows, np.array(bottom_borderin - sizeBV_half)))
shortlistedrows = np.hstack((shortlistedrows, np.array(bottom_border - sizeBV_half)))

shortlistedcolumns = np.hstack((shortlistedcolumns, np.array(left_border + sizeBH_half)))
shortlistedcolumns = np.hstack((shortlistedcolumns, np.array(left_borderin + sizeBH_half)))
shortlistedcolumns_temp = ShortlistedColumns(selectedcolumns, sizeBV)
shortlistedcolumns = np.hstack((shortlistedcolumns, shortlistedcolumns_temp))
shortlistedcolumns = np.hstack((shortlistedcolumns, np.array(right_borderin - sizeBH_half)))
shortlistedcolumns = np.hstack((shortlistedcolumns, np.array(right_border - sizeBH_half)))

first = 1
for shortlistedrow in shortlistedrows:
    tempimage = np.array([], dtype = np.int64)
    for shortlistedcolumn in shortlistedcolumns:
        tempimage = np.hstack((tempimage, np.array(blackwhite_image[shortlistedrow][shortlistedcolumn])))
    if(first == 1):
        finalimage = np.hstack((finalimage, tempimage))
        first = 0
    else:
        finalimage = np.vstack((finalimage, tempimage))
    
cv2.imwrite('output.png', np.asarray(finalimage))













