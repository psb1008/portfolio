#Template Matching을 사용한 방식
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

src = cv2.imread("data1/s5.png", cv2.IMREAD_GRAYSCALE)
templit_ = cv2.imread("data1/p5.PNG", cv2.IMREAD_GRAYSCALE)
resultimg = cv2.imread("data1/p5.PNG", cv2.IMREAD_COLOR)

cv2.namedWindow('image')
cv2.imshow('image', src)
click = False  # Mouse 클릭된 상태 (false = 클릭 x / true = 클릭 o) : 마우스 눌렀을때 true로, 뗏을때 false로
x1, y1 = -1, -1

# Mouse Callback함수 : 파라미터는 고정됨.
def draw_rectangle(event, x0, y0, flags, param):
    global x1, y1, click  # 전역변수 사용

    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스를 누른 상태
        click = True
        x1, y1 = x0, y0
        print("사각형의 왼쪽위 설정 : (" + str(x1) + ", " + str(y1) + ")")

    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동
        if click == True:  # 마우스를 누른 상태 일경우
            draw = src.copy()
            cv2.rectangle(draw, (x1, y1), (x0, y0), (255, 255, 255), 1)
            print("(" + str(x1) + ", " + str(y1) + "), (" + str(x0) + ", " + str(y0) + ")")
            cv2.imshow('image', draw)

    elif event == cv2.EVENT_LBUTTONUP:
        click = False;  # 마우스를 때면 상태 변경
        draw = src.copy()
        dst = templit_.copy()
        cv2.rectangle(draw, (x1, y1), (x0, y0), (255, 255, 255), 1)
        imgh = y0 - y1
        imgw = x0 - x1
        templit = np.zeros((imgh, imgw), np.uint8)
        hh = 0
        for h in range(y1, y0):
            ww = 0
            for w in range(x1, x0):
                value = src[h, w]
                templit[hh, ww] = value
                ww+=1
            hh+=1
        cv2.imshow('templit', templit)
        result = cv2.matchTemplate(dst, templit, cv2.TM_SQDIFF_NORMED)

        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        x, y = minLoc
        h, w = templit.shape
        dst = cv2.rectangle(resultimg, (x + 10, y + 10), (x + w - 10, y + h - 10), (0, 255, 0), 1)
        cv2.imshow("dst", dst)
        print("max matching rage : " + str(minVal))

cv2.setMouseCallback('image',draw_rectangle)

cv2.waitKey()
cv2.destroyAllWindows()
