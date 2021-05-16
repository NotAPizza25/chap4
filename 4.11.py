import numpy as np, cv2

def onChangeRad(value1):              # 반지름 조절 트랙바 콜백함수
    global title, image, rad

    rad = rad + value1
    cv2.imshow(title, image)


def onChangeThick(value2):            # 선 굵기 조절 트랙바 콜백 함수
    global title, image, thickness

    thickness = thickness + value2
    cv2.imshow(title, image)



def onMouse(event, x, y, flags, param):                     # 마우스 콜백 함수
    global title, image, rad, thickness
    rec = (x, y, 30, 30)

    if event == cv2.EVENT_RBUTTONDOWN:                                  # 원
        cv2.circle(image,(x,y), rad, 0, thickness )
        cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONDOWN:                                # 사각형
        cv2.rectangle(image, rec, (255, 0 ,0), thickness)
        cv2.imshow(title, image)

image = np.full((1000, 1500, 3), (255, 255, 255), np.uint8)
rad = 20
thickness = 1

title = 'proble 4.10'
cv2.imshow(title, image)

cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar('Radius', title,0 , 50, onChangeRad)
cv2.createTrackbar('Thickness', title,0, 10, onChangeThick)
cv2.waitKey(0)
