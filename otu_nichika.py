import cv2
import numpy as np

def BGR2GRAY(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()

    #Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)

    return out

def otsu_binalization(img , th = 128):
    max_sigma = 0
    max_t = 0
    print(img.shape)
    H,W = img.shape

    #determine threshhold
    for _t in range(1, 255):
        v0 = out[np.where(out < _t)]
        print('v0')
        print(v0)
        m0 = np.mean(v0) if len(v0) > 0 else 0.
        print('m0')
        print(m0)
        w0 = len(v0) / (H*W)
        v1 = out[np.where(out >= _t)]
        m1 = np.mean(v1) if len(v1) > 0 else 0.
        w1 = len(v1) / (H*W)
        sigma = w0 * w1 * ((m0 - m1)**2)
        if sigma > max_sigma:
            max_sigma = sigma
            max_t = _t

    #Binarization
    print('threshhold >> ', max_t)
    th = max_t
    out[out < th] = 0
    out[out >= th] = 255

    return out

if __name__ == '__main__':
    img = cv2.imread("imori.jpg").astype(np.float32)
    # Grayscale
    out = BGR2GRAY(img)
    # Otsu's binarization
    out = otsu_binalization(out)

    # Save result
    cv2.imwrite("out.jpg", out)
    cv2.imshow("result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
