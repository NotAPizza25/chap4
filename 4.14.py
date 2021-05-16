import numpy as np                          # 마우스 이벤트 및 그리기 종합 예제
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_MBUTTONDOWN:
        if pt[0] < 0: pt = (x,y)                                #시작 좌표 지정
        else:

            size =(float((pt[0] - x)/2), float((pt[1] - y)/2))
            center =((pt[0] - x)/2, (pt[1] - y)/2)

            cv2.imshow(title, image)
            pt = (-1, -1)                                       # 시작 좌표 초기화


white, black = (255, 255, 255), (0, 0, 0)
image = np.full((300, 500, 3), white, np.uint8)


pt = (-1, -1)                                   #시작 좌표 초기화
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)