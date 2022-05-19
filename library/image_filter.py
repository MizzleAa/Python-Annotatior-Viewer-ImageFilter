from library.utils.header import *

from library.images.bright_dark import BrightDark
from library.images.sharp_blur import SharpBlur
from library.images.reverse import Reverse
from library.images.contrast import Contrast
from library.images.roi import Roi

from library.utils.abstract import AbstractFilter


class ImageFilter():
    def __init__(self):
        self.bit8 = Bit8()
        self.bit16 = Bit16()
        self.bit24 = Bit24()

class Bit8(AbstractFilter):

    def __init__(self):
        self._bright_dark = BrightDark()
        self._sharp_blur = SharpBlur()
        self._reverse = Reverse()
        self._contrast = Contrast()
        self._roi = Roi()

    def bright_dark(self, data, options={}):
        image = self._bright_dark.bit8(data, options)
        return image
    
    def sharp_blur(self, data, options={}):
        image = self._sharp_blur.bit8(data, options)
        return image
    
    def reverse(self, data, options={}):
        image = self._reverse.bit8(data, options)
        return image
    
    def roi(self, data, options={}):
        image = self._roi.bit8(data, options)
        return image
    
    def contrast(self, data, options={}):
        image = self._contrast.bit8(data, options)
        return image
    

class Bit16(AbstractFilter):
    
    def __init__(self):
        self._bright_dark = BrightDark()
        self._sharp_blur = SharpBlur()
        self._reverse = Reverse()
        self._contrast = Contrast()
        self._roi = Roi()
        
    def bright_dark(self, data, options={}):
        image = self._bright_dark.bit16(data, options)
        return image
    
    def sharp_blur(self, data, options={}):
        image = self._sharp_blur.bit16(data, options)
        return image
    
    def reverse(self, data, options={}):
        image = self._reverse.bit16(data, options)
        return image
    
    def roi(self, data, options={}):
        image = self._roi.bit16(data, options)
        return image
    
    def contrast(self, data, options={}):
        image = self._contrast.bit16(data, options)
        return image
    

class Bit24(AbstractFilter):
    
    def __init__(self):
        self._bright_dark = BrightDark()
        self._sharp_blur = SharpBlur()
        self._reverse = Reverse()
        self._contrast = Contrast()
        self._roi = Roi()
        
    def bright_dark(self, data, options={}):
        image = self._bright_dark.bit24(data, options)
        return image
    
    def sharp_blur(self, data, options={}):
        image = self._sharp_blur.bit24(data, options)
        return image
    
    def reverse(self, data, options={}):
        image = self._reverse.bit24(data, options)
        return image
    
    def roi(self, data, options={}):
        image = self._roi.bit24(data, options)
        return image
    
    def contrast(self, data, options={}):
        image = self._contrast.bit24(data, options)
        return image
    
