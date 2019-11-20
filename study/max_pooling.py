#画像をある固定長の領域に分割し,
#各領域(セル)の平均値でその領域の値を埋めることをPoolingという
#CNNでは重要な考え方

import numpy as np
import cv2

def max_pooling(img,G=8):
    out = img.copy()

    H,W,C = img.shape
    Nh = int(H / G)
    Nw = int(W / G)
    print('H,W,C',H,W,C)

    for y in range(Nh):
        #print('y',y)
        for x in range(Nw):
            #print('y,x',y,x)
            for c in range(C):
                print(out[G*y:G*(y+1),G*x:G*(x+1),c])
                out[G*y:G*(y+1),G*x:G*(x+1),c] = np.max(out[G*y:G*(y+1),G*x:G*(x+1),c])
                print(out[G*y:G*(y+1),G*x:G*(x+1),c])
    return out

"""
before pooling
[[ 39  40  28  95 170 105  35  35]
 [ 50  41  39  52 109  97  87  55]
 [ 39  39  44  46  44  41  60  49]
 [ 38  39  37  48  46  37  37  38]
 [ 36  38  37  26  48  43  44  29]
 [ 41  34  43  50  48  38  38  36]
 [ 48  37  44  76  65  58  35  33]
 [ 70  87  94  83  94  94  71  39]]
 after pooling
[[170 170 170 170 170 170 170 170]
 [170 170 170 170 170 170 170 170]
 [170 170 170 170 170 170 170 170]
 [170 170 170 170 170 170 170 170]
 [170 170 170 170 170 170 170 170]
 [170 170 170 170 170 170 170 170]
 [170 170 170 170 170 170 170 170]
 [170 170 170 170 170 170 170 1
"""
#Read image
img = cv2.imread("imori.jpg")
#Average Pooling
out = max_pooling(img)

cv2.imwrite("out.jpg", out)
cv2.imshow("result",out)
cv2.waitKey(0)
