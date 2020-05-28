import cv2
import numpy as np
from preprocess_fun import *

image = cv2.imread('maze.jpg')
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

preprocessed = CreateImage(blackwhite_image, shortlistedrows, shortlistedcolumns)
cv2.imwrite('output1.jpg', preprocessed)

start_row, start_column, end_row, end_column = FindEnEx(preprocessed)
if(start_row == -1 or start_column == -1 or end_row == -1 or end_column == -1):
    print('Error:Not able to find entry and exit')
    exit()

solution_ip = preprocessed // 255
solution_ip = 1 - solution_ip
input_height, input_width = solution_ip.shape
SIZE = input_height
solution = [[0]*SIZE for _ in range(SIZE)]

def solvemaze(r, c):
    #if destination is reached, maze is solved
    #destination is the last cell(maze[SIZE-1][SIZE-1])
    if (r == end_row) and (c == end_column):
        solution[r][c] = 1;
        return True;
    #checking if we can visit in this cell or not
    #the indices of the cell must be in (0,SIZE-1)
    #and solution[r][c] == 0 is making sure that the cell is not already visited
    #maze[r][c] == 0 is making sure that the cell is not blocked
    if r>=0 and c>=0 and r<SIZE and c<SIZE and solution[r][c] == 0 and solution_ip[r][c] == 0:
        #if safe to visit then visit the cell
        solution[r][c] = 1
        #going down
        if solvemaze(r+1, c):
            return True
        #going right
        if solvemaze(r, c+1):
            return True
        #going up
        if solvemaze(r-1, c):
            return True
        #going left
        if solvemaze(r, c-1):
            return True
        #backtracking
        solution[r][c] = 0;
        return False;
    return 0;

if(solvemaze(start_row,start_column)):
    for column in range(0, input_width - 1):
        for row in range(0, input_height - 1):
            if(solution[row][column] == 1):
                preprocessed[row][column] = 128
                    
    arr = np.array(preprocessed) 
    cv2.imwrite('output2.jpg', preprocessed)
else:
    print ("No solution")








