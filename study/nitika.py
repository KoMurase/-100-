import cv2
import numpy as np

#二値化はグレースケールにしてから後, 二値化.

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

def binaryzation(img, th=128):

    img[img<th]=0
    img[img>=th]=255

    return img

img = cv2.imread('imori.jpg')
cv2.imshow('first',img )
out = gray_scaling(img)
out = binaryzation(out)
cv2.imwrite('out.jpg',out)
cv2.imshow('result',out )
cv2.waitKey(0)
