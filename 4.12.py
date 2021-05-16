import numpy as np                      # 트랙바 이벤트 사용 예제
import cv2

def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    image = image + add_value
    cv2.imshow(title, image)


image = np.zeros((300,500), np.uint8)

title = 'Trackbar Event'
cv2.imshow(title, image)
cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)

switch_case = {
    2424832:
        if (image[0][0] < 246): image = image +1
        cv2.setTrackbarPose('Brightness', title, image[0][0])
        cv2.imshow(title, image)
}

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.waitKey(0)
cv2.destroyAllWindos()