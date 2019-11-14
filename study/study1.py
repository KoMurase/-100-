import cv2


def BGR2RGB(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()
    cv2.imshow('r',r)

    #change
    img[:,:,0] = r
    img[:,:,1] = g
    img[:,:,2] = b

    return img

img = cv2.imread("rainbow.png")
cv2.imshow('first',img)
img = BGR2RGB(img)
cv2.imwrite('out.jpg',img)
cv2.imshow('result',img)
cv2.waitKey(0)
