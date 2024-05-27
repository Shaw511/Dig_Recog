import cv2
import numpy as np

# 读取输入图像
img = cv2.imread('input_image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化处理
ret, thresh = cv2.threshold(gray, 127, 255, 0)

# 寻找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 遍历轮廓
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

# 显示结果
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
