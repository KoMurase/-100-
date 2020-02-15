import numpy as np
import cv2

def motion_filter(img, K_size=3):
    H, W, C = img.shape

    #kernel
    K = np.zeros((H+pad*2,W+pad*2,C),dtype=np.float)
    out[pad: pad + H, pad: pad+W] = img.copy().astype(np.float)
    tmp = out.copy()

    #filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y,pad+x,c] = np.sum(K*tmp[y:y + K_size,x:x+K_size,c])
    out = out[pad: pad+H,pad:pad+W].astype(np.uint8)
