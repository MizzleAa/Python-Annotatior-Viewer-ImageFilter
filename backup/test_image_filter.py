from arsene_image_filter import GetImageType

from PIL import Image
import shutil
import os
import numpy as np

def roi(proc,img):
    options = {
        'roi': [0, 0, 500, 500]
    }
    img = proc.apply_hist_equal(img, options)
    return img

def reverse(proc,img):
    # 색상반전
    img = proc.apply_color_inversion(img)
    return img

def brightness(proc,img):
    # # 밝기
    options = {
        'n': 1
    }
    img = proc.apply_brightness(img, options)
    return img


def darktness(proc,img):
    # # 밝기
    options = {
        'n': -1
    }
    img = proc.apply_brightness(img, options)
    return img

def sharpenss(proc,img):
    # 선명도
    options = {
        'n': 1
    }
    img = proc.apply_sharpness(img, options)
    return img


def blur(proc,img):
    # 선명도
    options = {
        'n': -1
    }
    img = proc.apply_sharpness(img, options)
    return img

def save(img, dst_path, filename):
    # 이미지 저장
    image = Image.fromarray(img)
    # image = image.convert('RGBA')
    image.save(dst_path, 'tiff')

    w, h = image.size
    image.show(f'{filename} / w: {w} / h: {h}')


def filter_image(src_dir: str, dst_dir: str, filename: str):
    
    arsene = GetImageType()
    src_path = f'{src_dir}{filename}'
    dst_path = f'{dst_dir}{filename}'

    os.makedirs(dst_dir, exist_ok=True)
    shutil.copy(src_path, dst_path)

    proc, img = arsene.get_proc(src_path)

    #
    img = img//255
    #img = img.astype(np.uint8)
    #

    img = sharpenss(proc,img)
    save(img,dst_path, filename)
    img = darktness(proc,img)
    save(img,dst_path, filename)

    # "file_path": "/media/f51f00b9-461d-4bd4-86ab-e106cd562c2f/image/20220517181011_800009301814_V_emblem_yvessaintlaurent.png"


if __name__ == '__main__':
    
    src_dir = 'image/'
    dst_dir = 'image-filter/'
    # filename = '20220406112135_333_002123783249_20211013_02_0101_05.JPG'
    filename = '20220513175048_3008.png'
    filter_image(src_dir, dst_dir, filename)
