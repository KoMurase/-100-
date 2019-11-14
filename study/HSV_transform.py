import cv2
import numpy as np
#HSV変換とは、Hue(色相)、Saturation(彩度)、Value(明度)
# で色を表現する手法である。
#Hue : 色合いを360度で表現したもの
#Saturation : 色の鮮やかさ
#Value : 色の明るさ (高いほど白に近く、低いほど黒に近い)

#BGR -> HSV
def BGR2HSV(_img):
    """
    Max = max(R,G,B)
    Min = min(R,G,B)
    H =  { 0                            (if Min=Max)
           60 x (G-R) / (Max-Min) + 60  (if Min=B)
           60 x (B-G) / (Max-Min) + 180 (if Min=R)
           60 x (R-B) / (Max-Min) + 300 (if Min=G)
    V = Max
    S = Max - Min
    """
    img = _img.copy() / 255.
    hsv = np.zeros_like(img , dtype=np.float32)
    #get max and min
    max_v = np.max(img, axis=2).copy()
    min_v = np.min(img, axis=2).copy()
    min_arg = np.argmin(img, axis=2)
    #H
    hsv[... , 0][np.where(max_v == min_v)]=0
    print(hsv)
    # if min == B
    ind = np.where(min_arg == 0)
    hsv[... , 0][ind] = 60 * (img[...,1][ind] - img[...,2][ind])/ (max_v[ind] - min_v[ind]) + 60
    # if min == R
    ind = np.where(min_arg == 0)
    hsv[... , 0][ind] = 60 * (img[...,0][ind] - img[...,1][ind])/ (max_v[ind] - min_v[ind]) + 180
    # if min == G
    ind = np.where(min_arg == 1)
    hsv[..., 0][ind] = 60 * (img[..., 2][ind] - img[..., 0][ind])/ (max_v[ind] - min_v[ind]) + 300
    # S
    hsv[..., 1] = max_v.copy() - min_v.copy()
    #V
    hsv[..., 2] = max_v.copy()

    return hsv

if __name__ == '__main__':
    # Read image
    img = cv2.imread("imori.jpg").astype(np.float32)
    cv2.imshow("imori.jpg", img)
    # RGB > HSV
    hsv = BGR2HSV(img)

    # Transpose Hue
    #hsv[..., 0] = (hsv[..., 0] + 180) % 360

    # HSV > RGB
    #out = HSV2BGR(img, hsv)

    # Save result
    cv2.imwrite("HSV.jpg", hsv)
    cv2.imshow("result", hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
