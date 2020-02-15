"""
ガウシアンフィルタとは平滑化の一種であり、また、ノイズ除去に
も使われる
ガウシアンフィルタは注目画素の周辺画素をガウス分布による重みづけで
平滑化する.このような重みをカーネルやフィルタと呼ばれる.
ただし,画像の端はこのままではフィルタリングできないため,
画素が足りない部分では, 0で埋める.これを0パディングといい、
かつ、重みを正規化する.
"""

import cv2
import numpy as np

#Gaussian filter
def gaussian_filter(img, K_size=3,sigma=1.3):
    if len(img.shape) == 3:
        H,W,C = img.shape
    else:
        img = np.expand_dims(img,axis=-1)
        H,W,C = img.shape

    ##Zero padding
    pad = K_size // 2
    out = np.zeros
