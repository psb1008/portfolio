#Hough Transfer 사용한 각도 측정
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
img = cv2.imread('data1/s2.JPG')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

imgsize = img.shape
imgh = imgsize[0]
imgw = imgsize[1]

insp = np.zeros((imgh, imgw), np.uint8)

for h in range(0, imgh):
    for w in range(0, imgw):
        if binary[h, w] == 255:
            insp[h, w] = gray[h, w]

edges = cv2.Canny(insp,50,150,apertureSize = 3)

minLineLength = 50
maxLineGap = 10

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
    # 두점 각도 계산
    p1 = (x1,y1)
    p2 = (x2,y2)
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    res = np.rad2deg((ang1 - ang2) % (2 * np.pi))

    res = math.atan2((y1 - y2), (x1 - x2)) / np.pi * 180
    print("Degree : " + str(res))

cv2.imshow('original', gray)
cv2.imshow('binary', binary)
cv2.imshow('insp', insp)
cv2.imshow('edges', edges)
cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()