import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('mazemachine.h5')

img = np.empty((1, 21, 21), dtype='float16')

img[0] = cv2.imread('input.png', 0)/255
img = np.reshape(img, (1, 21, 21, 1))

classes = model.predict(img)
classes = np.reshape(classes, (21,21))*255
#classes[classes < 50] = 0     
#classes[classes > 50] = 255    
cv2.imwrite('output.png', np.asarray(classes))