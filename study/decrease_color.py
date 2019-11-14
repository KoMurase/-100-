#Q.6 減色処理
import numpy as np
import cv2

def decrease_color(img):
    out = img.copy()

    out = out // 64 * 64 + 32

    return out

#Read image
img = cv2.imread("imori.jpg")

#Dicrease color
out = dicrease_color(img)

cv2.imwrite("out.jpg", out)
cv2.imshow("result",out)
cv2.waitkey(0)
 
