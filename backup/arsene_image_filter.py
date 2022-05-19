from abc import abstractmethod, ABCMeta

import os
import numpy as np
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
from scipy import signal, ndimage


class GetImageType:
    '''
    'path': 이미지 경로를 받아 이미지와 이미지타입에 맞는 필터 클래스 반환
    '''

    def get_proc(self, path: str):
        if not os.path.exists(path):
            return None, None

        img = Image.open(path)
        mode = img.mode
        filter_class = None

        if mode == 'L':
            options = {
                'mode': mode,
                'number_bins': pow(2, 8)
            }
            filter_class = IntImageFilterProc(options)

            np_thresh = np.zeros_like(img)
            np_thresh[img > 127] = 255
            img = np_thresh

        elif (mode == 'I') or (mode == 'I;16') or (mode == 'F'):
            options = {
                'mode': 'I;16',
                'number_bins': pow(2, 16)
            }
            filter_class = IntImageFilterProc(options)

            img = np.array(img, dtype='uint16')

        elif (mode == 'RGB') or (mode == 'RGBA'):
            img = np.array(img, dtype='uint8')

            filter_class = RGBImageFilterProc()

        return filter_class, img


class ImageFilterProc(metaclass=ABCMeta):

    # ROI 평준화
    @abstractmethod
    def apply_hist_equal(self, img, options):
        pass

    # 대조
    @abstractmethod
    def apply_contrast(self, img, options):
        pass

    # 밝기
    @abstractmethod
    def apply_brightness(self, img, options):
        pass

    # 색상반전
    @abstractmethod
    def apply_color_inversion(self, img):
        pass

    # 선명도
    @abstractmethod
    def apply_sharpness(self, img, options):
        pass

    def get_cumsum(self, img, options):
        '''
        options = {
            "roi": [x,y,w,h],
            "number_bins": int
        }
        '''
        roi = options['roi']
        number_bins = options['number_bins']
        if roi is not None:
            x = roi[0]
            y = roi[1]
            width = roi[2]
            height = roi[3]
            roi_img = img[y: y + height, x: x + width]
        else:
            roi_img = img

        hist, bins = np.histogram(roi_img, number_bins)
        cdf = hist.cumsum()
        cdf = number_bins * cdf / cdf[-1]
        return cdf, bins

    def sharpness(self, img, options):
        '''
        options = {
            "n": int
        }
        '''
        
        n = options['n']
        #img = img//255
        kernel = np.array([
            [-1.0, -1.0, -1.0, -1.0, -1.0],
            [-1.0, +2.0, +2.0, +2.0, -1.0],
            [-1.0, +2.0, +9.0, +2.0, -1.0],
            [-1.0, +2.0, +2.0, +2.0, -1.0],
            [-1.0, -1.0, -1.0, -1.0, -1.0],
        ]) / 9.0
        for _ in range(n):
            img = signal.convolve2d(img, kernel, mode='same', boundary='fill', fillvalue=0)
        
        # img = img.astype(np.uint8)
        # min_value = np.finfo(img.dtype).min
        # max_value = np.finfo(img.dtype).max

        # img = (img-min_value)/(max_value-min_value)

        # min_value = np.finfo(img.dtype).min
        # max_value = np.finfo(img.dtype).max
        
        # img = np.asarray(img, dtype=np.uint16)
        
        return img

    def blur(self, img, options):
        '''
        options = {
            "n": int
        }
        '''
        n = options['n']
        img = ndimage.gaussian_filter(img, 3 * abs(n))
        return img


class IntImageFilterProc(ImageFilterProc):
    def __init__(self, options):
        '''
        options = {
            "mode": str,
            "number_bins": int
        }
        '''
        self.number_bins = options['number_bins']
        self.mode = options['mode']

    def apply_hist_equal(self, img, options):
        '''
        options = {
            "roi": [x,y,w,h]
        }
        '''
        options = {
            'roi': options['roi'],
            'number_bins': self.number_bins - 1
        }
        cdf, bins = self.get_cumsum(img, options)
        equalized = np.interp(img.flatten(), bins[:-1], cdf)
        return equalized.reshape(img.shape)

    def apply_contrast(self, img, options):
        '''
        options = {
            "n": int
        }
        '''
        n = options['n']
        if self.number_bins > 256:
            return img * (1 + (n / 5.0))
        else:
            im = Image.fromarray(img, mode=self.mode)
            enhance = ImageEnhance.Contrast(im)
            im = enhance.enhance(max(0, 1 + (n / 10)))
            return np.array(im)

    def apply_brightness(self, img, options):
        '''
        options = {
            "n": int
        }
        '''
        n = options['n']
        if self.number_bins > 500:
            if img.dtype == np.uint16:
                img = np.int32(img)
                img += n * 5000
                img[img >= self.number_bins] = self.number_bins - 1
                img[img < 0] = 0
                img = np.uint16(img)
            else:
                img += n * 5000
            return img
        else:
            im = Image.fromarray(img, mode=self.mode)
            enhance = ImageEnhance.Brightness(im)
            im = enhance.enhance(max(0, 1 + (n / 10)))
            return np.array(im)

    def apply_color_inversion(self, img):
        im = Image.fromarray(img)
        white_img = Image.new(im.mode, im.size, self.number_bins - 1)
        white_arr = np.array(white_img)
        return white_arr - img

    def apply_sharpness(self, img, options):
        '''
        options = {
            "n": int
        }
        '''
        n = options['n']
        if n > 0:
            return self.sharpness(img, options)
        else:
            return self.blur(img, options)


class RGBImageFilterProc(ImageFilterProc):
    def apply_hist_equal(self, img, options):
        '''
        options = {
            "roi": [x,y,w,h]
        }
        '''
        roi = options['roi']

        rgb_img = Image.fromarray(img, mode='RGB')
        y_cb_cr_img = rgb_img.convert('YCbCr')
        (y, cb, cr) = y_cb_cr_img.split()

        options = {
            'roi': roi,
            'number_bins': 255
        }
        cdf, _ = self.get_cumsum(img, options)

        lut = np.arange(256, dtype='uint8')
        for i in range(len(cdf)):
            lut[i] = int(cdf[i])
        y_list = np.array(y)
        y_list = lut[np.uint8(y_list)]
        y = Image.fromarray(y_list, mode='L')

        y_cb_cr_img = Image.merge('YCbCr', (y, cb, cr))
        rgb_img = y_cb_cr_img.convert('RGB')

        return np.array(rgb_img)

    def apply_contrast(self, img, options):
        '''
        options = {
            "n": int
        }
        '''
        n = options['n']

        im = Image.fromarray(img, mode='RGB')
        enhance = ImageEnhance.Contrast(im)
        im = enhance.enhance(max(0, 1 + (n / 10)))
        return np.array(im)

    def apply_brightness(self, img, options):
        '''
        options = {
            "n": int
        }
        '''
        n = options['n']

        im = Image.fromarray(img, mode='RGB')
        enhance = ImageEnhance.Brightness(im)
        im = enhance.enhance(max(0, 1 + (n / 10)))
        return np.array(im)

    def apply_color_inversion(self, img):
        im = ImageOps.invert(Image.fromarray(img))
        return np.array(im)

    def apply_sharpness(self, img, options):
        '''
        options = {
            "n": int
        }
        '''
        n = options['n']

        im = Image.fromarray(img, mode='RGB')
        if n > 0:
            for _ in range(n):
                im = im.filter(ImageFilter.SHARPEN)
        else:
            im = im.filter(ImageFilter.GaussianBlur(2 * abs(n)))
        return np.array(im)
