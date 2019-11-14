#Y = 0.2126 R + 0.7152 G + 0.0722 B
import cv2
import numpy as np
def gray_scaling(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()

    out = 0.2126*r + 0.7152*g + 0.0722*b
    out = out.astype(np.uint8)

    return out

img = cv2.imread('imori.jpg')
cv2.imshow('first',img )
out = gray_scaling(img)
cv2.imwrite('out.jpg',out)
cv2.imshow('result',out )
cv2.waitKey(0)
