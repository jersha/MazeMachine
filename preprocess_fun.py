import cv2

def BlackWhite(input_image):
    grey_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    (thresh, output_image) = cv2.threshold(grey_image, 50, 255, cv2.THRESH_BINARY)
    return output_image

def FindLB(input_image):
    input_height, input_width = input_image.shape
    top_border_array = []
    bottom_border_array = []
    left_border_array = []
    right_border_array = []
    width_left = input_width // 4
    width_center = (input_width // 4) * 2
    width_right = (input_width // 4) * 3
    height_left = input_height // 4
    height_center = (input_height // 4) * 2
    height_right = (input_height // 4) * 3
    top_border = -1
    bottom_border = -1
    left_border = -1
    right_border = -1
    
    pixel = 0
    while input_image[pixel][width_left] != 0 and pixel < (input_height - 2):
        pixel += 1
    top_border_array.append(pixel)
    
    pixel = 0
    while input_image[pixel][width_center] != 0 and pixel < (input_height - 2):
        pixel += 1
    top_border_array.append(pixel)
    
    pixel = 0
    while input_image[pixel][width_right] != 0 and pixel < (input_height - 2):
        pixel += 1
    top_border_array.append(pixel)
    
    left_center = abs(top_border_array[0] - top_border_array[1])
    left_right = abs(top_border_array[0] - top_border_array[2])
    center_right = abs(top_border_array[1] - top_border_array[2])
    
    if(left_center < 5):
        top_border = top_border_array[0]
    elif(left_right < 5):
        top_border = top_border_array[0]
    elif(center_right < 5):
        top_border = top_border_array[1]
    
    pixel = input_height - 1
    while input_image[pixel][width_left] != 0 and pixel > 0:
        pixel -= 1
    bottom_border_array.append(pixel)
    
    pixel = input_height - 1
    while input_image[pixel][width_center] != 0 and pixel > 0:
        pixel -= 1
    bottom_border_array.append(pixel)
    
    pixel = input_height - 1
    while input_image[pixel][width_right] != 0 and pixel > 0:
        pixel -= 1
    bottom_border_array.append(pixel)
    
    left_center = abs(bottom_border_array[0] - bottom_border_array[1])
    left_right = abs(bottom_border_array[0] - bottom_border_array[2])
    center_right = abs(bottom_border_array[1] - bottom_border_array[2])
    
    if(left_center < 5):
        bottom_border = bottom_border_array[0]
    elif(left_right < 5):
        bottom_border = bottom_border_array[0]
    elif(center_right < 5):
        bottom_border = bottom_border_array[1]
    
    pixel = 0
    while input_image[height_left][pixel] != 0 and pixel < (input_width - 2):
        pixel += 1
    left_border_array.append(pixel)
    
    pixel = 0
    while input_image[height_center][pixel] != 0 and pixel < (input_width - 2):
        pixel += 1
    left_border_array.append(pixel)
    
    pixel = 0
    while input_image[height_right][pixel] != 0 and pixel < (input_width - 2):
        pixel += 1
    left_border_array.append(pixel)
    
    left_center = abs(left_border_array[0] - left_border_array[1])
    left_right = abs(left_border_array[0] - left_border_array[2])
    center_right = abs(left_border_array[1] - left_border_array[2])
    
    if(left_center < 5):
        left_border = left_border_array[0]
    elif(left_right < 5):
        left_border = left_border_array[0]
    elif(center_right < 5):
        left_border = left_border_array[1]
    
    pixel = input_width - 1
    while input_image[height_left][pixel] != 0 and pixel > 0:
        pixel -= 1
    right_border_array.append(pixel)
    
    pixel = input_width - 1
    while input_image[height_center][pixel] != 0 and pixel > 0:
        pixel -= 1
    right_border_array.append(pixel)
    
    pixel = input_width - 1
    while input_image[height_right][pixel] != 0 and pixel > 0:
        pixel -= 1
    right_border_array.append(pixel)
    
    left_center = abs(right_border_array[0] - right_border_array[1])
    left_right = abs(right_border_array[0] - right_border_array[2])
    center_right = abs(right_border_array[1] - right_border_array[2])
    
    if(left_center < 5):
        right_border = right_border_array[0]
    elif(left_right < 5):
        right_border = right_border_array[0]
    elif(center_right < 5):
        right_border = right_border_array[1]
    
    return top_border, bottom_border, left_border, right_border

def FindSizeB(input_image, top_border):
    input_height, input_width = input_image.shape
    width_left = input_width // 4
    width_center = (input_width // 4) * 2
    width_right = (input_width // 4) * 3
    black_size_array = []
    black_size = -1
    
    pixel = top_border
    while input_image[pixel][width_left] == 0 and pixel < (input_height - 2):
        pixel += 1
    black_size_array.append(pixel - top_border)
    
    pixel = top_border
    while input_image[pixel][width_center] == 0 and pixel < (input_height - 2):
        pixel += 1
    black_size_array.append(pixel - top_border)
    
    pixel = top_border
    while input_image[pixel][width_right] == 0 and pixel < (input_height - 2):
        pixel += 1
    black_size_array.append(pixel - top_border)
    
    left_center = abs(black_size_array[0] - black_size_array[1])
    left_right = abs(black_size_array[0] - black_size_array[2])
    center_right = abs(black_size_array[1] - black_size_array[2])
    
    if(left_center < 5):
        black_size = black_size_array[0]
    elif(left_right < 5):
        black_size = black_size_array[0]
    elif(center_right < 5):
        black_size = black_size_array[1]
        
    return black_size

def FindSizeW(input_image, white_start):
    input_height, input_width = input_image.shape
    width_left = input_width // 4
    width_center = (input_width // 4) * 2
    width_right = (input_width // 4) * 3
    white_size_array = []
    white_size = -1
    
    pixel = white_start
    while input_image[pixel][width_left] != 0 and pixel < (input_height - 2):
        pixel += 1
    white_size_array.append(pixel - white_start)
    
    pixel = white_start
    while input_image[pixel][width_center] == 0 and pixel < (input_height - 2):
        pixel += 1
    white_size_array.append(pixel - white_start)
    
    pixel = white_start
    while input_image[pixel][width_right] == 0 and pixel < (input_height - 2):
        pixel += 1
    white_size_array.append(pixel - white_start)
    
    left_center = abs(white_size_array[0] - white_size_array[1])
    left_right = abs(white_size_array[0] - white_size_array[2])
    center_right = abs(white_size_array[1] - white_size_array[2])
    
    if(left_center < 5):
        white_size = white_size_array[0]
    elif(left_right < 5):
        white_size = white_size_array[0]
    elif(center_right < 5):
        white_size = white_size_array[1]
        
    return white_size