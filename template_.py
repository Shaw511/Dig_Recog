import cv2
import numpy as np

# 读取输入图像和模板图像
img = cv2.imread('input_image.jpg', 0)
template = cv2.imread('template_image.jpg', 0)

# 获得模板图像的高度和宽度
w, h = template.shape[::-1]

# 使用模板匹配法进行匹配
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

# 在输入图像上标记匹配的位置
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# 显示结果
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()