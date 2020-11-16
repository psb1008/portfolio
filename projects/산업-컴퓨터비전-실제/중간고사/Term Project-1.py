import cv2
import numpy as np

img = cv2.imread('data/1.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, (300,200))
cv2.imshow('img', img)

#Grab Cut
y = x = 1
w, h = img.shape[1], img.shape[0]

labels = np.zeros(img.shape[:2], np.uint8)
labels, bgdModel, fgModel = cv2.grabCut(img, labels,
    (x, y, w-2, h-2), None, None, 5, cv2.GC_INIT_WITH_RECT)

grabcut = np.copy(img)
grabcut[(labels == cv2.GC_PR_BGD) | (labels == cv2.GC_PR_BGD)] //= 3

#Color to Gray(uint8)
imgGray = cv2.cvtColor(grabcut, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', imgGray)
#Binary
_, imgBinary = cv2.threshold(imgGray, 180, 255, cv2.THRESH_BINARY)
#cv2.imshow('binary', imgBinary)
#cv2.imwrite('data/temp.png', imgBinary)

#imgTemp = cv2.imread('data/temp.png', cv2.IMREAD_COLOR)
#imgGray1 = cv2.cvtColor(imgTemp, cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(imgGray1, 50, 150, apertureSize=3)

lines = cv2.HoughLinesP(imgGray, 1, np.pi/180, 140, 100, 10)[0]

dbg_img = np.zeros((imgGray.shape[0], imgGray.shape[1], 3), np.uint8)

for x1, y1, x2, y2 in lines:
    print('Detected line: ({} {}) ({} {})'.format(x1, y1, x2, y2))
    cv2.line(dbg_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('image1', dbg_img)
cv2.waitKey()
cv2.destroyAllWindows()