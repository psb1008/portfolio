import numpy as np                                                      #numpy(ver1.19.2) import / python(3.9.2)
import tensorflow as tf                                                 #tensorflow(ver2.4.1) import / Cuda Toolkit(ver11.0)
from tensorflow.keras.datasets import mnist                             #tensorflow.keras.database module에 mnist 메소드 사용
from tensorflow.keras.models import Sequential                          #tensorflow.keras.models module에 Sequential 메소드 사용
from tensorflow.keras.layers import Dense                               #tensorflow.keras.layers module에 Dense 메소드 사용
from tensorflow.keras.optimizers import Adam                            #tensorflow.keras.optimizers module에 Adam 메소드 사용

(x_train, y_train), (x_test, y_test) = mnist.load_data()                #mnist.load_data() -> 학습데이터와 테스트데이터로 구성
x_train = x_train.reshape(60000, 784)                                   #60000x28x28(3차원텐서) -> 60000x784(2차원텐서) 
x_test = x_test.reshape(10000, 784)                                     #10000x28x28(3차원텐서) -> 10000x784(2차원텐서)
x_train = x_train.astype(np.float32)/255.0                              #0 ~ 1 사이로 정규화 (이유 : feautre 값의 범위 차가 크면 오차함수가 최저지점에 수렴하는데 시간이 오래 걸림, 즉 정확도가 떨어짐)
x_test = x_test.astype(np.float32)/255.0                                #동일
y_train = tf.keras.utils.to_categorical(y_train,10)                     #원핫코드로 변환
y_test = tf.keras.utils.to_categorical(y_test,10)                       #원핫코드로 변환

n_input=784
n_hidden1=1024
n_hidden2=512
n_hidden3=512
n_hidden4=512
n_output=10

#MLP구현
mlp=Sequential()                                                        #Sequential 모델 : layer를 층층이 쌓아 올릴 수 있는 방법
mlp.add(Dense(units=n_hidden1,activation='tanh',input_shape=(n_input,),kernel_initializer='random_uniform',bias_initializer='zeros')) #input layer
#Dense Layer        : 입력과 출력층을 모두 연결해 준다
#units              : 현재 layer에 대한 노드 개수 
#activation         : 활성화 함수
#input_shape        : 입력 Tensor
#kernel_initializer : weight 초기화 (random_uniform : -0.05 ~ 0.05 사이의 임의의 값으로 설정)
#bias_initializer   : bias 설정
   
mlp.add(Dense(units=n_hidden2,activation='tanh',kernel_initializer='random_uniform',bias_initializer='zeros')) #hidden layer
mlp.add(Dense(units=n_hidden3,activation='tanh',kernel_initializer='random_uniform',bias_initializer='zeros')) #hidden layer
mlp.add(Dense(units=n_hidden4,activation='tanh',kernel_initializer='random_uniform',bias_initializer='zeros')) #hidden layer
mlp.add(Dense(units=n_output,activation='tanh',kernel_initializer='random_uniform',bias_initializer='zeros'))  #output layer

#학습수행
mlp.compile(loss='mean_squared_error',optimizer=Adam(learning_rate=0.001),metrics=['accuracy'])
#loss           : 손실함수 (MSE 사용)
#optimizer      : 손실율을 줄이기 위한 최적의 weight을 찾는 과정
#metrics        : 학습 도중 손실함수 값 측정 옵션
hist=mlp.fit(x_train,y_train,batch_size=128,epochs=30,validation_data=(x_test,y_test),verbose=2)
#x_trian, y_train : 훈련집합
#batch_size       : 훈렵집합을 batch size 만큼 묶어서 가중치 업데이트
#epochs           : 반복할 세대 수 (학습 횟수)
#verbose          : 학습 진행상태 표기 (0- silent, 1- progres bar, 2-one line per epoch)
   
#ex) 학습데이터 60,000 / batch size 128 = 469번의 가중치 업데이트가 일어남
#epochs 30, 총 30번의 학습을 진행

res=mlp.evaluate(x_test,y_test,verbose=0) #평가 : 테스트 데이터를 통해 정확률 확인
print("정확률은",res[1]*100)

import matplotlib.pyplot as plt

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.grid()
plt.show()

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.grid()
plt.show()