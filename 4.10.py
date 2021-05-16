import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title, image
    rec = (x, y, 30, 30)

    if event == cv2.EVENT_RBUTTONDOWN:                                  # 원
        cv2.circle(image,(x,y), 20, 0 )
        cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONDOWN:                                # 사각형
        cv2.rectangle(image, rec, (255, 0 ,0))
        cv2.imshow(title, image)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

title = 'proble 4.10'
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
