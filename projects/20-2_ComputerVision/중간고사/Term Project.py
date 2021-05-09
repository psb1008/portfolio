import cv2
import numpy as np
import matplotlib.pyplot as plt

image0 = cv2.imread('data/1.png', 0).astype(np.float32) / 255
image90 = cv2.imread('data/2.png', 0).astype(np.float32) / 255
imageR = cv2.imread('data/3.png', 0).astype(np.float32) / 255

#fft 변환
fft0 = cv2.dft(image0, flags=cv2.DFT_COMPLEX_OUTPUT)
fft90 = cv2.dft(image90, flags=cv2.DFT_COMPLEX_OUTPUT)
fftR = cv2.dft(imageR, flags=cv2.DFT_COMPLEX_OUTPUT)

shifted0 = np.fft.fftshift(fft0, axes=[0,1])
shifted90 = np.fft.fftshift(fft90, axes=[0,1])
shiftedR = np.fft.fftshift(fftR, axes=[0,1])

magnitude0 = cv2.magnitude(shifted0[:, :, 0], shifted0[:, :, 1])
magnitude0 = np.log(magnitude0)
magnitude90 = cv2.magnitude(shifted90[:, :, 0], shifted90[:, :, 1])
magnitude90 = np.log(magnitude90)
magnitudeR = cv2.magnitude(shiftedR[:, :, 0], shiftedR[:, :, 1])
magnitudeR = np.log(magnitudeR)

#Sobel
dxy0 = cv2.Sobel(magnitude0, cv2.CV_32F, 1, 1)
dxy90 = cv2.Sobel(magnitude90, cv2.CV_32F, 1, 1)
dxyR = cv2.Sobel(magnitudeR, cv2.CV_32F, 1, 1)

#부동소수점 영상 변환
dst0 = (dxy0).astype(np.uint8)
dst90 = (dxy90).astype(np.uint8)
dstR = (dxyR).astype(np.uint8)

#edges = cv2.Canny(dst0, 50, 150, apertureSize = 3)
#cv2.imshow('', edges)

#lines = cv2.HoughLinesP(dst0, 1, np.pi/180, 100, 100, 10)[0]

#dbg_img = np.zeros((dst0.shape[0], dst0.shape[1], 3), np.uint8)
#for x1, y1, x2, y2 in lines:
#    print('Detected line: ({} {}) ({} {})'.format(x1, y1, x2, y2))
#    cv2.line(dbg_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

plt.subplot(341)
plt.axis('off')
plt.imshow(image0, cmap='gray')
plt.subplot(342)
plt.axis('off')
plt.imshow(magnitude0, cmap='gray')
plt.subplot(343)
plt.axis('off')
plt.imshow(dxy0, cmap='gray')
plt.subplot(344)
plt.axis('off')
plt.imshow(dst0, cmap='gray')
plt.subplot(345)
plt.axis('off')
plt.imshow(image90, cmap='gray')
plt.subplot(346)
plt.axis('off')
plt.imshow(magnitude90, cmap='gray')
plt.subplot(347)
plt.axis('off')
plt.imshow(dxy90, cmap='gray')
plt.subplot(348)
plt.axis('off')
plt.imshow(dst90, cmap='gray')
plt.subplot(349)
plt.axis('off')
plt.imshow(imageR, cmap='gray')
plt.subplot(3,4,10)
plt.axis('off')
plt.imshow(magnitudeR, cmap='gray')
plt.subplot(3,4,11)
plt.axis('off')
plt.imshow(dxyR, cmap='gray')
plt.subplot(3,4,12)
plt.axis('off')
plt.imshow(dstR, cmap='gray')

plt.show()