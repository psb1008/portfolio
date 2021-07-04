import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from tensorflow.keras.optimizers import Adam

# MNIST 데이터셋을 읽고 신경망에 입력할 형태로 변환
(x_train,y_train),(x_test,y_test)=mnist.load_data() #MNIST Dataset Load
x_train=x_train.reshape(60000,28,28,1)              #전체 Data중 60,000개를 학습용으로 사용. 28x28 Size의 8bit(1Byte) Gray Scale 영상
x_test=x_test.reshape(10000,28,28,1)                #전체 Data중 10,000개를 Test용으로 사용. 28x28 Size의 8bit(1Byte) Gray Scale 영상
x_train=x_train.astype(np.float32)/255.0            #Train Data를 ndarray로 변환
x_test=x_test.astype(np.float32)/255.0              #Test Data를 ndarray로 변환
y_train=tf.keras.utils.to_categorical(y_train,10)   #원핫코드로 변환
y_test=tf.keras.utils.to_categorical(y_test,10)     #원핫코드 : 각 단어에 고유한 인덱스를 부여. 표현하고 싶은 단어의 인덱스의 위치에 1을 부여,
                                                    #         다른 단어의 인덱스의 위치에는 0을 부여.

# 신경망 모델 설계
cnn=Sequential()                              #Sequential 모델 시작
# 구조 : Conv - Conv - MaxPooling - Dropout - FC - Dropout - FC
# MaxPooling : 맥스 풀링은 Activation map을 MxN의 크기로 잘라낸(Pooling) 후, 그 안에서 가장 큰 값을(Max) 뽑아내는 방법
# Dropout : 뉴런을 임의로 삭제하면서 학습. 오버피팅(over-fit)을 막기 위한 방법.
# FC : Fully Connected Layer. Convolution/Pooling 프로세스의 결과를 취하여 이미지를 정의된 라벨로 분류하는 데 사용
cnn.add(Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)))
cnn.add(Conv2D(64,(3,3),activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2,2)))
cnn.add(Dropout(0.25))
cnn.add(Flatten())
cnn.add(Dense(128,activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(10,activation='softmax'))

# 신경망 모델 학습
cnn.compile(loss='categorical_crossentropy',optimizer=Adam(),metrics=['accuracy'])
   # Loos Func.은 categorical_crossentropy
   # categorical_crossentropy : 다중 분류 손실함수. one-hot encoding 클래스
   # 		            출력값이 one-hot encoding 된 결과로 나오고 실측 결과와의 비교시에도 실측 결과는 one-hot encoding 형태로 구성
   # Optimizer(Neural Network를 구성하는 알고리즘을 최적화시켜주는 도구) : Adam(Momentum과 RMSProp를 융합한 방법)
   # metric(평가지표를 의미) : Accuracy(정확률)
hist=cnn.fit(x_train,y_train,batch_size=128,epochs=12,validation_data=(x_test,y_test),verbose=2)
   # batch_size 128, epochs 12, verbose 2
   # batch_size : 몇 개의 샘플로 가중치를 갱신할 것인지 지정
   # epochs : 학습 반복 횟수
   # verbose : 얼마나 자세하게 정보를 표시할 것인가를 지정

# 신경망 모델 정확률 평가
res=cnn.evaluate(x_test,y_test,verbose=2)
print("정확률은",res[1]*100)

import matplotlib.pyplot as plt

# 정확률 그래프
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'], loc='best')
plt.grid()
plt.show()

# 손실 함수 그래프
   #손실함수 : 신경망 성능의 '나쁨'을 나타내는 지표. 일반적으로는 평균 제곱 오차와 교차 엔트로피 오차를 사용
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'], loc='best')
plt.grid()
plt.show()