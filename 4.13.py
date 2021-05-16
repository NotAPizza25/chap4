import cv2                                      #영상파일 읽기 (컬러) 예제
from Common.utils import print_matInfo      # 행렬 정보 출력 함수 import

title1, title2 = 'color2gray', 'color2color'
color2gray = cv2.imread("images/read_color.jpg", cv2.IMREAD_GRAYSCALE)
color2color = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)
if color2gray is None or color2color is None:               #예외처리
    raise Exception("영상파일 읽기 에러")

## 행렬을 윈도우에 명암도 영상으로 표시
print("행렬 좌표(100,100) 화소값")
print("%s %s" % (title1, color2gray[100,100]))

print_matInfo(title1, color2gray)
cv2.imshow(title1, color2gray)


## 영상 파일 저장
params_jpg = (cv2.IMWRITE_JPEG_QUALITY,100)                      # JPEG 화질 설정
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]                   # PNG 압축 레벨 설정

## 행렬을 영상파일로 저장
print("처리 중")
cv2.imwrite("images/write_test2.jpg", color2gray, params_jpg)        # 지정한 화질로 저장
cv2.imwrite("images/write_test3.png", color2gray, params_png)
print("저장 완료")

cv2.waitKey(0)