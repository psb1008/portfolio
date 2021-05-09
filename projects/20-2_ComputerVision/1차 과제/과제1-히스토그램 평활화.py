import cv2
import numpy as np
import matplotlib.pyplot as plt

def equlizehist(src, ch):
    plt.figure(figsize=(15, 8))
    plt.subplot(131)
    plt.title('Before')
    hist, bins = np.histogram(src[:, :, ch], 256, [0, 255])
    plt.fill_between(range(256), hist, 0)
    plt.subplot(132)
    plt.title('After')
    src[..., ch] = cv2.equalizeHist(src[..., ch])
    hist, bins = np.histogram(src[..., ch], 256, [0, 255])
    plt.fill_between(range(256), hist, 0)
    plt.subplot(133)
    plt.title('Result')
    plt.imshow(src)
    plt.show()


src = cv2.imread('data/image_Baboon512rgb.png')
cv2.imshow('input', src)
finish = False
while not finish:
    print('R,G,B 중 변화 시킬 채널을 입력하시오')
    copy = np.copy(src)
    key = cv2.waitKey(0)
    if key == ord('r'):
        equlizehist(copy, 0)
    elif key == ord('g'):
        equlizehist(copy, 1)
    elif key == ord('b'):
        equlizehist(copy, 2)
    elif key == 27:
        finish = True
