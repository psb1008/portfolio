import cv2
import numpy as np
import matplotlib.pyplot as plt

print('Bilateral filtering을 위한')
diameter = int(input('diameter를 입력하세요 : '))
sigmaColor = float(input('SigmaColor를 입력하세요 : '))
sigmaSpace = int(input('SigmaSpace를 입력하세요 : '))

src = cv2.imread('data/image_F16_512rgb.png').astype(np.float32) / 255

noised = (src + 0.2 * np.random.rand(*src.shape).astype(np.float32))
noised = noised.clip(0, 1)
plt.figure(figsize=(10, 5))
plt.suptitle('Bilateral')
plt.subplot(121)
plt.axis('off')
plt.title('Before(Noise Image)')
plt.imshow(noised[:, :, [2, 1, 0]])
bilat = cv2.bilateralFilter(noised, diameter, sigmaColor, sigmaSpace)
plt.subplot(122)
plt.axis('off')
titleName = 'After : diameter(' + str(diameter) + ') ' + 'sigmaColor(' + str(sigmaColor) + ') ' + 'sigmaSpace(' + str(sigmaSpace) + ')'
plt.title(titleName)
plt.imshow(bilat[:, :, [2, 1, 0]])
plt.show()
