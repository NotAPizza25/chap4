import numpy as np
import cv2

mat1 = np.full((200, 300), 0, np.uint8)
mat2 = np.full((200, 300), 0, np.uint8)


title1, title2 = 'win mode1', 'win mode2'
cv2.moveWindow(title1, 0, 0)
cv2.moveWindow(title2, 300, 200)

cv2.imshow(title1, mat1)
cv2.imshow(title2, mat2)
cv2.waitKey(0)
cv2.destroyAllWindows()