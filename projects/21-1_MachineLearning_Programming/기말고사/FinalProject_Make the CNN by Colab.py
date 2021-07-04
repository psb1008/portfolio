# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:52:45 2021

@author: psb
"""

import tensorflow as tf      
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Activation, Dense
from tensorflow.keras.layers import Flatten, Convolution2D, MaxPooling2D
from tensorflow.keras.models import load_model
import cv2
import numpy as np

import time
from google.colab import drive
drive.mount('/content/drive')
data_dir = '/content/drive/My Drive/img_data.npy'


start = time.time()  # 시작 시간 저장

X_train, X_test, Y_train, Y_test = np.load(data_dir, allow_pickle=True)

categories = ["normal","reject"]
num_classes = len(categories)
 
model = Sequential()
model.add(Convolution2D(16, (3, 3), padding='same', activation='relu', input_shape=X_train.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
  
model.add(Convolution2D(64, (3, 3),  activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
 
model.add(Convolution2D(64, (3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
  
model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation = 'softmax'))
  
model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['accuracy'])
hist = model.fit(X_train, Y_train, batch_size=32, epochs=30, validation_data=(X_test, Y_test), verbose=2)

print(hist.history.keys())

#model.save('Gersang.h5')

# 신경망 모델 정확률 평가
res=model.evaluate(X_test,Y_test,verbose=0)
print("정확률은",res[1]*100)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

import matplotlib.pyplot as plt

# 정확률 그래프
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'],loc='best')
plt.grid()
plt.show()

# 손실 함수 그래프
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'],loc='best')
plt.grid()
plt.show()

