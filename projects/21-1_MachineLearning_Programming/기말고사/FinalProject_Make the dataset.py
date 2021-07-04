import os, re, glob
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

groups_folder_path = './CNN_Sample/' #Image data path
categories = ["normal","reject"]

num_classes = len(categories)

image_w = 56
image_h = 56

x = []
y = []

for idex, categroie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idex] = 1
    image_dir = groups_folder_path + categroie + '/'
    
    for top, dir, f in os.walk(image_dir):
        for filename in f:
            print(image_dir+filename)
            img = cv2.imread(image_dir+filename)
            img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
            x.append(img/256)
            y.append(label)
  
print(np.shape(x))
print(np.shape(y))    
print(y[0])    
x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x, y)
xy = (x_train, x_test, y_train, y_test)

np.save("./img_data_56x56.npy",xy)



