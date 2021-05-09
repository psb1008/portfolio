import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('img/mypicture.jpg')

plt.imshow(img)
plt.show()