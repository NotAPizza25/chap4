import numpy as np, cv2

image = np.zeros((600, 400,3), np.uint8)
image.fill(255)

red = (0, 0, 255)
rec = (100, 100, 200, 300)
cv2.rectangle(image, rec, red, 1  )

title = 'problem 4.9'
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
