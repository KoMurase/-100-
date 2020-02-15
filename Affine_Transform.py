import matplotlib.pyplot as plt
from skimage import transform, data
import cv2

class image_trans:
    def __init__(self):
        print('aa')
    def image_show(img):
        print(img.shape)
        h, w, c = img.shape
        plt.figure(figsize = [float(w/100), float(h/100)])
        plt.title(f'w={w}, h={h}')
        plt.imshow(img)
        plt.xticks([])
        plt.yticks([])
        plt.show()

    def affine_trans(img):
        """
        scikit-imageでアフィン変換を試す
        transform.AffineTransformクラスのインスタンスを作成
        transform.warpで画像に上記インスタンスの効果を適用する

        [transform.AffineTransformの引数]
        scale : 拡大縮小(縦・横のタプルで与える。マイナスで反転)
        translation : 平行移動(縦・横のタプルで与える)
        rotation : 回転
        shear : 剪断変形(せんだん)

        [transform.warpの引数]
        第1引数：画像データ
        第2引数： transform.AffineTransformクラス等のインスタンス
        """
        print('type of img:',type(img))
        print('元画像を表示します')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow('',img)
        cv2.waitKey()

        print('画像の拡大')
        AT = transform.AffineTransform(scale=(0.8,0.8))
        warp_img = transform.warp(img,AT)
        cv2.imshow('',warp_img)
        cv2.waitKey()

        print('画像の縮小')
        AT = transform.AffineTransform(scale=(1.2,1.2))
        warp_img = transform.warp(img,AT)
        cv2.imshow('',warp_img)
        cv2.waitKey()

        # 平行移動のみ
        at = transform.AffineTransform(translation=(-30,-50))
        warp_img = transform.warp(img,at)
        cv2.imshow('',warp_img)
        cv2.waitKey()

        #反転と平行移動
        at = transform.AffineTransform(scale=(-1,1),translation=(640, 0))
        warp_img = transform.warp(img,at)
        cv2.imshow('',warp_img)
        cv2.waitKey()

        # 回転と平行移動
        at = transform.AffineTransform(rotation=0.5,translation=(300,-100))
        warp_img = transform.warp(img,at)
        cv2.imshow('',warp_img)
        cv2.waitKey()

        # 剪断変形と拡大縮小、平行移動
        at = transform.AffineTransform(shear=1,scale=(1.5,1.5),translation=(30,30))
        warp_img = transform.warp(img,at)
        cv2.imshow('',warp_img)
        cv2.waitKey()



test = image_trans()
#imt = img_trans()
filename = './ironman.jpg'
ironman = cv2.imread(filename,cv2.IMREAD_COLOR)
#このまま表示しようとすると赤色が青色になって表示されてしまった
#BGRの画像をRGBにする
ironman = cv2.cvtColor(ironman, cv2.COLOR_BGR2RGB)
print(ironman)
print('image.shape:',ironman.shape)
#image_trans.image_show(ironman)

image_trans.affine_trans(ironman)
