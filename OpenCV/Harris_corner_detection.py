import cv2
import numpy as np

img_cv2 = cv2.imread('./sample/100_harris.jpg')
img_gray = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
img_gray_32 = np.float32(img_gray)

dst = cv2.cornerHarris(img_gray_32, blockSize=7, ksize=11, k=0.045)
dst = cv2.dilate(dst, None)
img_cv2[dst > 0.3*dst.max()] = [0, 0, 255]

cv2.imshow('dst', img_cv2)
cv2.waitKey(0)
cv2.imwrite('./sample/100_harris_out.jpg', img_cv2)


