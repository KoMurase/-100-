#max_min　フィルタ
#フィルタ内の最大値と最小値の差を出力するフィルタであり,
#エッジ検出のフィルタの一つである
import cv2
import numpy as np

#Gray scale
def BGR2GRAY(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()

    #Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)

    return out

def max_min_filter(img, K_size=3):
    if len(img.shape) == 3:
        H,W,C = img.shape

        #zero padding
        pad = K_size // 2
        out = np.zeros((H+pad*2, W+pad*2,3), astype=np.float)
        out[pad: pad+H, pad: pad+W] = img.copy().astype(np.float)
        tmp = out.copy()

        #filtering
        for y in range(H):
            for x in range(W):
                for c in range(3):
                    out[pad+y, pad+x,c] = np.max(tmp[y:y+K_size,x:x+K_size])-np.min(tmp[y:y+K_size,x:x+K_size])
        out = out[pad: pad+H, pad: pad+W].astype(np.uint8)

    return out

# Read image
img = cv2.imread("imori.jpg").astype(np.float)

# grayscale
gray = BGR2GRAY(img)

# Max-Min filtering
out = max_min_filter(gray, K_size=3)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
