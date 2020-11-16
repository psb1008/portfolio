import cv2
import numpy as np
import matplotlib.pyplot as plt

mask_size = int(input('mask size를 입력하세요'))

chk = False
flag = 1
while not chk:
    flag = int(input('1(High-Pass) 또는 2(Low-Pass)를 입력하세요'))
    if 0 < flag < 3:
       chk = True
    else:
        print('1 or 2 중 하나를 입력하세요')


image = cv2.imread('data/image_Lena512rgb.png', 0).astype(np.float32) / 255
fft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)
fft_shift = np.fft.fftshift(fft, axes=[0, 1])


mask = np.zeros(image.shape, np.uint8)
center = (image.shape[0]//2, image.shape[1]//2)
cv2.circle(mask, center, mask_size, 255, cv2.FILLED)

if flag == 1:
    mask = cv2.bitwise_not(mask)

fft_shift[:, :, 0] *= mask
fft_shift[:, :, 1] *= mask

fft = np.fft.ifftshift(fft_shift, axes=[0, 1])

filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
mask_new = np.dstack((mask, np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)))

plt.figure(figsize=(15, 8))
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.title('no high frequencies')
plt.imshow(filtered, cmap='gray')
plt.subplot(133)
plt.axis('off')
plt.title('mask')
plt.imshow(mask, cmap='gray')
plt.show()