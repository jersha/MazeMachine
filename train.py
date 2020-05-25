from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras.losses import binary_crossentropy
from tensorflow.keras.optimizers import Adam
import cv2
import numpy as np

# Model configuration
batch_size = 50
img_width, img_height, img_num_channels = 21, 21, 1
loss_function = binary_crossentropy
no_epochs = 100
optimizer = Adam()
validation_split = 0.2
verbosity = 1

#image preprocessing
x_train = np.empty((700, 21, 21), dtype='float16')
y_train = np.empty((700, 21, 21), dtype='float16')
x_validation = np.empty((200, 21, 21), dtype='float16')
y_validation = np.empty((200, 21, 21), dtype='float16')
x_test = np.empty((100, 21, 21), dtype='float16')
y_test = np.empty((100, 21, 21), dtype='float16')


for i in range(700):
    x_train[i] = cv2.imread('mazes/in_train/input{}.png'.format(i), 0)/255
    y_train[i] = cv2.imread('mazes/out_train/output{}.png'.format(i), 0)/255
x_train = np.reshape(x_train, (700, 21, 21, 1))
y_train = np.reshape(y_train, (700, 441))

j = 0  
for i in range(700, 900):
    x_validation[j] = cv2.imread('mazes/in_validation/input{}.png'.format(i), 0)/255
    y_validation[j] = cv2.imread('mazes/out_validation/output{}.png'.format(i), 0)/255
    j += 1
x_validation = np.reshape(x_validation, (200, 21, 21, 1))
y_validation = np.reshape(y_validation, (200, 441))

j = 0     
for i in range(900, 1000):
    x_test[j] = cv2.imread('mazes/in_test/input{}.png'.format(i), 0)/255
    y_test[j] = cv2.imread('mazes/out_test/output{}.png'.format(i), 0)/255
    j += 1
x_test = np.reshape(x_test, (100, 21, 21, 1))
y_test = np.reshape(y_test, (100, 441))

# Determine shape of the data
input_shape = (img_width, img_height, img_num_channels)

# Create the model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(441, activation='sigmoid'))
    
# Compile the model
model.compile(loss=loss_function,
              optimizer=optimizer,
              metrics=['accuracy'])

# Fit data to model
history = model.fit(x_train, y_train,
            batch_size=batch_size,
            epochs=no_epochs,
            verbose=verbosity,
            validation_data=(x_validation, y_validation))

# Generate generalization metrics
score = model.evaluate(x_test, y_test, verbose=0)
print(f'Test loss: {score[0]} / Test accuracy: {score[1]}')

model.save('mazemachine.h5')