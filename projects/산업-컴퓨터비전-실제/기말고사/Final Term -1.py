#Histogram 방식
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

img = cv2.imread('data1/s5.PNG', cv2.IMREAD_COLOR)
cv2.namedWindow('image')
cv2.imshow('image', img)
click = False  # Mouse 클릭된 상태 (false = 클릭 x / true = 클릭 o) : 마우스 눌렀을때 true로, 뗏을때 false로
x1, y1 = -1, -1
lx, ly, rx, ry, tx, ty, bx, by = -1, -1, -1, -1, -1, -1, -1, -1
max_l, max_r = 0, 0

def MaxPeakInLine(x, y):
    global max_l, max_r

    arr = []
    for h in range(ty + 20, y):
        var = int(img[h, x, 0])
        arr.append(var)

    arr_mag = []
    for i in range(1, len(arr) - 1):
        mag = arr[i - 1] - arr[i]
        arr_mag.append(mag)
    max_l = arr_mag.index(max(arr_mag))

    arr_1 = []
    for h in range(y, by):
        var = int(img[h, x, 0])
        arr_1.append(var)

    arr_mag_1 = []
    for i in range(1, len(arr_1) - 1):
        mag = arr_1[i] - arr_1[i - 1]
        arr_mag_1.append(mag)
    max_r = arr_mag_1.index(max(arr_mag_1))

    plt.subplot(411)
    plt.plot(arr)
    plt.subplot(412)
    plt.plot(arr_mag)
    plt.subplot(413)
    plt.plot(arr_1)
    plt.subplot(414)
    plt.plot(arr_mag_1)
    plt.show()

def CalcRotateChip():
    global lx, ly, rx, ry, tx, ty, bx, by
    global max_l, max_r

    rotate = img.copy()
    x = int((rx - lx)/ 2) + lx
    y = int((by - ty) / 2) + ty

    MaxPeakInLine(x, y)
    c1 = max_l
    c2 = max_r
    #cv2.circle(rotate, (x, ty + c1 +20), 5, (255, 255, 255), 1)
    #cv2.circle(rotate, (x, y + c2), 5, (255, 255, 255), 1)
    MaxPeakInLine(x - 10, y)
    c3 = max_l
    c4 = max_r
    cv2.circle(rotate, (x - 10, ty + c3+30), 5, (255, 255, 255), 1)
    cv2.circle(rotate, (x - 10, y + c4), 5, (255, 255, 255), 1)
    MaxPeakInLine(x + 10, y)
    c5 = max_l
    c6 = max_r
    cv2.circle(rotate, (x + 10, ty + c5+30), 5, (255, 255, 255), 1)
    cv2.circle(rotate, (x + 10, y + c6), 5, (255, 255, 255), 1)

    cv2.line(rotate, (x - 10, ty + c3+30), (x + 10, ty + c5+30), (0,255,255), 3)
    cv2.line(rotate, (x - 10, y + c4), (x + 10, y + c6), (0, 255, 255), 3)

    #두점 각도 계산
    p1 = (x - 10, ty + c3+30)
    p2 = (x + 10, ty + c5+30)
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    res = np.rad2deg((ang1 - ang2) % (2 * np.pi))

    res = math.atan2((ty + c3+30) - (ty + c5+30), (x -10) - (x + 10))/np.pi * 180
    print("Degree : " + str(res))
    cv2.imshow('center point', rotate)

    print(str(c1) + ", " + str(c2) + ", " + str(c3) + ", " + str(c4) + ", " + str(c5) + ", " + str(c6))

def get_edge_point(draw, x0, x1, y0, y1, dir):
    global lx, ly, rx, ry, tx, ty, bx, by

    # ROI내 배열 합
    arr = []
    if dir == 0:
        for h in range(y1 + 1, y0 - 1):
            sum = 0
            count = 0
            for w in range(x1 + 1, x0 - 1):
                var = img[h, w, 0]
                sum += int(var)
            arr.append(sum)
             #   if(var > 100):
             #      sum += var
             #      count += 1
           # if(count != 0):
            #    arr.append(int(sum/count))
    elif dir == 1:
        for h in range(y1 + 1, y0 - 1):
            sum = 0
            count = 0
            for w in range(x1 + 1, x0 - 1):
                var = img[w, h, 0]
                sum += int(var)
            arr.append(sum)
                #if (var > 100):
                 #   sum += var
                 #   count += 1
           # if (count != 0):
              #  arr.append(int(sum/count))

    # 인접데이터의 평균?
    arrtemp = []
    for x in range(1, len(arr) - 1):
        avg = (arr[x - 1] + arr[x] + arr[x + 1]) / 3
        arrtemp.append(avg)
    # 미분
    arrmagitude = []
    arrmagitude_left = []
    arrmagitude_right = []
    for x in range(0, int(len(arrtemp) / 2)):
        magnitude = arrtemp[x + 1] - arrtemp[x]
        arrmagitude.append(magnitude)
        arrmagitude_left.append(magnitude)
    for x in range(int(len(arrtemp) / 2), len(arrtemp) - 1):
        magnitude = arrtemp[x - 1] - arrtemp[x]
        arrmagitude.append(magnitude)
        arrmagitude_right.append(magnitude)
    # 미분값 내림차순 후 first, second 값 추출
    max_left = arrmagitude_left.index(max(arrmagitude_left))
    max_right = arrmagitude_right.index(max(arrmagitude_right))
    max_right = len(arrmagitude_right) - max_right - 1
    leftpeak = int(y1 + max_left)
    rightpeak = int(y0 - max_right)

    if dir == 0:
        # 점찍기
        roi_width_center = int((x0 - x1) / 2) + x1
        cv2.circle(draw, (roi_width_center, leftpeak), 1, (255, 0, 0), 1)
        cv2.circle(draw, (roi_width_center, rightpeak), 1, (255, 0, 0), 1)
        tx = roi_width_center
        ty = leftpeak
        bx = roi_width_center
        by = rightpeak
    elif dir == 1:
        # 점찍기
        roi_width_center = int((x0 - x1) / 2) + x1
        cv2.circle(draw, (leftpeak, roi_width_center), 1, (255, 0, 0), 1)
        cv2.circle(draw, (rightpeak, roi_width_center), 1, (255, 0, 0), 1)
        lx = leftpeak
        ly = roi_width_center
        rx = rightpeak
        ry = roi_width_center

    plt.subplot(211)
    plt.plot(arrtemp)
    plt.subplot(212)
    plt.plot(arrmagitude)
    plt.show()

# Mouse Callback함수 : 파라미터는 고정됨.
def draw_rectangle(event, x0, y0, flags, param):
    global x1, y1, click  # 전역변수 사용
    global lx, ly, rx, ry, tx, ty, bx, by

    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스를 누른 상태
        click = True
        x1, y1 = x0, y0
        print("사각형의 왼쪽위 설정 : (" + str(x1) + ", " + str(y1) + ")")

    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동
        if click == True:  # 마우스를 누른 상태 일경우
            draw = img.copy()
            cv2.rectangle(draw, (x1, y1), (x0, y0), (0, 0, 0), 1)
            print("(" + str(x1) + ", " + str(y1) + "), (" + str(x0) + ", " + str(y0) + ")")
            cv2.imshow('image', draw)

    elif event == cv2.EVENT_LBUTTONUP:
        click = False;  # 마우스를 때면 상태 변경
        draw = img.copy()
        plt.clf()
        cv2.rectangle(draw, (x1, y1), (x0, y0), (0, 0, 0), 1)
        get_edge_point(draw, x0, x1, y0, y1, 0) #0 : hor
        get_edge_point(draw, y0, y1, x0, x1, 1) #1 : ver
        cv2.rectangle(draw, (lx, ty), (rx, by), (255, 255, 0), 1)
        cv2.imshow('image', draw)
        CalcRotateChip()

cv2.setMouseCallback('image',draw_rectangle)

cv2.waitKey()
cv2.destroyAllWindows()
