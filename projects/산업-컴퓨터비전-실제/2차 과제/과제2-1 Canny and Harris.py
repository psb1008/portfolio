import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread('data/stitching/s1.jpg')

edges1 = cv2.Canny(image1, 200, 100)

corners = cv2.cornerHarris(cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY), 2, 3, 0.04)
corners = cv2.dilate(corners, None)
show_img = np.copy(image1)
show_img[corners > 0.1 * corners.max()] = [0, 0, 255]

plt.figure(figsize=(10, 5))
plt.subplot(221)
plt.axis('off')
plt.title('original')
plt.imshow(image1[:,:,[2,1,0]])
plt.subplot(222)
plt.axis('off')
plt.title('canny')
plt.imshow(edges1, cmap='gray')
plt.subplot(223)
plt.axis('off')
plt.title('harris')
plt.imshow(corners, cmap='gray')
plt.subplot(224)
plt.axis('off')
plt.title('corner point')
plt.imshow(show_img[:,:,[2,1,0]])
plt.show()