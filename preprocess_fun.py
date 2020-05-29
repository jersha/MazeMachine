import cv2
import numpy as np
from sys import exit
    
def BlackWhite(input_image):
    grey_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    (thresh, output_image) = cv2.threshold(grey_image, 150, 255, cv2.THRESH_BINARY)
    return output_image

def FindBorder(input_image):
    input_height, input_width = input_image.shape
    top_border_array = np.array([], dtype = np.int64)
    bottom_border_array = np.array([], dtype = np.int64)
    left_border_array = np.array([], dtype = np.int64)
    right_border_array = np.array([], dtype = np.int64)
    top_border = -1
    bottom_border = -1
    left_border = -1
    right_border = -1
    
    for pixel_LR in range(input_width):
        for pixel_TB in range(input_height):
            value = input_image[pixel_TB][pixel_LR]
            if(value == 0):
                break
        top_border_array = np.hstack((top_border_array, np.array(pixel_TB)))
    top_border = np.bincount(top_border_array).argmax() 
    
    for pixel_LR in range(input_width):
        for pixel_BT in range(input_height - 1, 0, -1):
            value = input_image[pixel_BT][pixel_LR]
            if(value == 0):
                break
        bottom_border_array = np.hstack((bottom_border_array, np.array(pixel_BT)))
    bottom_border = np.bincount(bottom_border_array).argmax() 
    
    for pixel_TB in range(input_height):
        for pixel_LR in range(input_width):
            value = input_image[pixel_TB][pixel_LR]
            if(value == 0):
                break
        left_border_array = np.hstack((left_border_array, np.array(pixel_LR)))
    left_border = np.bincount(left_border_array).argmax() 

    for pixel_TB in range(input_height):
        for pixel_RL in range(input_width - 1, 0, -1):
            value = input_image[pixel_TB][pixel_RL]
            if(value == 0):
                break
        right_border_array = np.hstack((right_border_array, np.array(pixel_RL)))
    right_border = np.bincount(right_border_array).argmax() 
    
    if(top_border == -1 or bottom_border == -1 or left_border == -1 or right_border == -1):
        print('Error:Not able to find the border')
        exit()
    else:
        return top_border, bottom_border, left_border, right_border

def FindSizeB(input_image, top_border, bottom_border, left_border, right_border):
    input_height, input_width = input_image.shape
    black_size_arrayV = np.array([], dtype = np.int64)
    black_sizeV = -1
    black_size_arrayH = np.array([], dtype = np.int64)
    black_sizeH = -1
    
    for pixel_RL in range(left_border, right_border):
        count = 0
        for pixel_TB in range(top_border, bottom_border):
            value = input_image[pixel_TB][pixel_RL]
            if(value == 0):
                count += 1
            else: 
                break
        black_size_arrayV = np.hstack((black_size_arrayV, np.array(count)))
    black_sizeV = np.bincount(black_size_arrayV).argmax()
    
    for pixel_TB in range(top_border, bottom_border):
        count = 0
        for pixel_RL in range(left_border, right_border):
            value = input_image[pixel_TB][pixel_RL]
            if(value == 0):
                count += 1
            else: 
                break
        black_size_arrayH = np.hstack((black_size_arrayH, np.array(count)))
    black_sizeH = np.bincount(black_size_arrayH).argmax()
    
    if(black_sizeV == -1 or black_sizeH == -1):
        print('Error:Not able to find the size of Black')
        exit()
    else:
        return black_sizeV, black_sizeH

def RowsSelect(input_image, top_borderin, bottom_borderin, left_borderin, right_borderin, sizeBH):
    selectedrows = np.array([], dtype = np.int64)
    maxcount = 0
    for pixel_TB in range(top_borderin, bottom_borderin):
        count = 0
        previous = 0
        continuousB = np.array([], dtype = np.int64)
        for pixel_LR in range(left_borderin, right_borderin):
            value = input_image[pixel_TB][pixel_LR]
            if(value == 0):
                count += 1
            else:
                if(previous < count):
                    previous = count
                count = 0
        if(previous == 0):
             previous = count
        continuousB = np.hstack((continuousB, np.array(previous)))
        maxcount = np.amax(continuousB)
        if(maxcount > (2 * sizeBH)):
            selectedrows = np.hstack((selectedrows, np.array(pixel_TB)))
    return selectedrows

def ColumnssSelect(input_image, top_borderin, bottom_borderin, left_borderin, right_borderin, sizeBV):
    selectedcolumns = np.array([], dtype = np.int64)
    maxcount = 0
    for pixel_LR in range(left_borderin, right_borderin):
        count = 0
        previous = 0
        continuousB = np.array([], dtype = np.int64)
        for pixel_TB in range(top_borderin, bottom_borderin):
            value = input_image[pixel_TB][pixel_LR]
            if(value == 0):
                count += 1
            else:
                if(previous < count):
                    previous = count
                count = 0
        if(previous == 0):
             previous = count
        continuousB = np.hstack((continuousB, np.array(previous)))
        maxcount = np.amax(continuousB)
        if(maxcount > (2 * sizeBV)):
            selectedcolumns = np.hstack((selectedcolumns, np.array(pixel_LR)))
    return selectedcolumns

def ShortlistedRows(selectedrows, sizeBV_half, top_border, top_borderin, bottom_border, bottom_borderin):
    shortlistedrows_array = np.array([], dtype = np.int64)
    shortlistedrows_array = np.hstack((shortlistedrows_array, np.array(top_border + sizeBV_half)))
    shortlistedrows_array = np.hstack((shortlistedrows_array, np.array(top_borderin + sizeBV_half)))
    shortlistedrows_array = np.hstack((shortlistedrows_array, np.array(selectedrows[0] + sizeBV_half)))
    size = int(selectedrows.shape[0]) - 1
    for i in range(1, size):
        if(((selectedrows[i] - selectedrows[i - 1]) > 2) and ((selectedrows[i] + 1) == selectedrows[i + 1])):
            shortlistedrows_array = np.hstack((shortlistedrows_array, np.array(selectedrows[i] - sizeBV_half)))
            shortlistedrows_array = np.hstack((shortlistedrows_array, np.array(selectedrows[i] + sizeBV_half)))
    shortlistedrows_array = np.hstack((shortlistedrows_array, np.array(bottom_borderin - sizeBV_half)))
    shortlistedrows_array = np.hstack((shortlistedrows_array, np.array(bottom_border - sizeBV_half)))
    return shortlistedrows_array

def ShortlistedColumns(selectedcolumns, sizeBH_half, left_border, left_borderin, right_border, right_borderin):
    shortlistedcolumn_array = np.array([], dtype = np.int64)
    shortlistedcolumn_array = np.hstack((shortlistedcolumn_array, np.array(left_border + sizeBH_half)))
    shortlistedcolumn_array = np.hstack((shortlistedcolumn_array, np.array(left_borderin + sizeBH_half)))
    shortlistedcolumn_array = np.hstack((shortlistedcolumn_array, np.array(selectedcolumns[0] + sizeBH_half)))
    size = int(selectedcolumns.shape[0]) - 1
    for i in range(1, size):
        if((selectedcolumns[i] - selectedcolumns[i - 1]) > 2 and ((selectedcolumns[i] + 1) == selectedcolumns[i + 1])):
            shortlistedcolumn_array = np.hstack((shortlistedcolumn_array, np.array(selectedcolumns[i] - sizeBH_half)))
            shortlistedcolumn_array = np.hstack((shortlistedcolumn_array, np.array(selectedcolumns[i] + sizeBH_half)))
    shortlistedcolumn_array = np.hstack((shortlistedcolumn_array, np.array(right_borderin - sizeBH_half)))
    shortlistedcolumn_array = np.hstack((shortlistedcolumn_array, np.array(right_border - sizeBH_half)))
    return shortlistedcolumn_array
    
def CreateImage(input_image, shortlistedrows, shortlistedcolumns):
    finalimage = np.array([], dtype = np.int64)
    first = 1
    for shortlistedrow in shortlistedrows:
        tempimage = np.array([], dtype = np.int64)
        for shortlistedcolumn in shortlistedcolumns:
            tempimage = np.hstack((tempimage, np.array(input_image[shortlistedrow][shortlistedcolumn])))
        if(first == 1):
            finalimage = np.hstack((finalimage, tempimage))
            first = 0
        else:
            finalimage = np.vstack((finalimage, tempimage))
    return finalimage
    
def FindEnEx(finalimage):
    start_row = -1
    start_column = -1
    end_row = -1
    end_column = -1
    input_height, input_width = finalimage.shape
    row_no = 0
    for column_no in range(0, input_width - 1):
        if(finalimage[row_no][column_no] == 255):
            start_row = row_no
            start_column = column_no
            break
    
    if(start_row == -1):
        column_no = 0
        for row_no in range(0, input_height - 1):
            if(finalimage[row_no][column_no] == 255):
                start_row = row_no
                start_column = column_no
                break
    row_no = input_height - 1    
    for column_no in range(0, input_width - 1):
        if(finalimage[row_no][column_no] == 255):
            end_row = row_no
            end_column = column_no
            break
    
    if(end_row == -1):
        column_no = input_width - 1
        for row_no in range(0, input_height - 1):
            if(finalimage[row_no][column_no] == 255):
                end_row = row_no
                end_column = column_no
                break
    if(start_row == -1 or start_column == -1 or end_row == -1 or end_column == -1):
        print('Error:Not able to find entry and exit')
        exit()
    else:
        return start_row, start_column, end_row, end_column
    
def Print_details(top_border, bottom_border, left_border, right_border, sizeBV, sizeBH):
    print('top_border = ', top_border)
    print('bottom_border = ', bottom_border)
    print('left_border = ', left_border)
    print('right_border = ', right_border)
    print('SizeBlackVertical = ', sizeBV)
    print('SizeBlackHorizontal = ', sizeBH)