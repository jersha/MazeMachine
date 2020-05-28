import cv2
import numpy as np
from sys import exit
from preprocess_fun import *

def BlackWhite(input_image):
    grey_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    (thresh, output_image) = cv2.threshold(grey_image, 150, 255, cv2.THRESH_BINARY)
    return output_image

image = cv2.imread('output1.jpg')
maze = BlackWhite(image) // 255
print(maze[27][76], maze[27][0])
maze = 1 - maze

input_height, input_width = maze.shape
SIZE = input_height

#list to store the solution matrix
solution = [[0]*SIZE for _ in range(SIZE)]

#function to solve the maze
#using backtracking
def solvemaze(r, c):
    #if destination is reached, maze is solved
    #destination is the last cell(maze[SIZE-1][SIZE-1])
    if (r==31) and (c==55):
        solution[r][c] = 1;
        return True;
    #checking if we can visit in this cell or not
    #the indices of the cell must be in (0,SIZE-1)
    #and solution[r][c] == 0 is making sure that the cell is not already visited
    #maze[r][c] == 0 is making sure that the cell is not blocked
    if r>=0 and c>=0 and r<SIZE and c<SIZE and solution[r][c] == 0 and maze[r][c] == 0:
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


if(solvemaze(0,30)):
                    
    arr = np.array(solution) 
    cv2.imwrite('output2.jpg', np.asarray(arr))
else:
    print ("No solution")