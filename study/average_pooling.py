#画像をある固定長の領域に分割し,
#各領域(セル)の平均値でその領域の値を埋めることをPoolingという
#CNNでは重要な考え方

import numpy as np
import cv2

def average_pooling(img,G=8):
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
                print('y,x,c',y,x,c)
                print(out[G*y:G*(y+1),G*x:G*(x+1),c])
                out[G*y:G*(y+1),G*x:G*(x+1),c] = np.mean(out[G*y:G*(y+1),G*x:G*(x+1),c]).astype(np.int)
                print(out[G*y:G*(y+1),G*x:G*(x+1),c])

"""
before pooling
[[ 81  91  74  71  65  59  68 110]
 [ 90  89  82  74  66  60  60  99]
 [ 83  73  74  72  71  71  65  95]
 [ 89  74  69  71  69  68  68  85]
 [ 92  83  73  72  67  60  80  93]
 [ 79  85  77  76  71  64  98 112]
 [ 79  87  84  81  83  73  90  95]
 [ 82  85  88  83  94  85  74  66]]
 after pooling
[[78 78 78 78 78 78 78 78]
 [78 78 78 78 78 78 78 78]
 [78 78 78 78 78 78 78 78]
 [78 78 78 78 78 78 78 78]
 [78 78 78 78 78 78 78 78]
 [78 78 78 78 78 78 78 78]
 [78 78 78 78 78 78 78 78]
 [78 78 78 78 78 78 78 78]]
"""
#Read image
img = cv2.imread("imori.jpg")

#Average Pooling
out = average_pooling(img)

cv2.imwrite("out.jpg", out)
cv2.imshow("result",out)
cv2.waitkey(0)
