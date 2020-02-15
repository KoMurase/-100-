import cv2
import numpy as np

# mean filter
def mean_filter(img, K_size=3):
    H, W, C = img.shape

    # Kernel
    K = np.diag([1] * K_size).astype(np.float)
    K /= K_size
    
    #zero padding
    pad
