from library.utils.header import *
from library.utils.abstract import AbstractBit

class SharpBlur(AbstractBit):
    def bit8(self, data, options={}):
        option_level = options["level"]
        
        if option_level > 0:
            data = self._sharp(data,option_level)
        if option_level < 0:
            data = self._blur(data,option_level)
        
        return data
    
        
    def bit16(self, data, options={}):
        option_level = options["level"]
        
        if option_level > 0:
            data = self._sharp(data,option_level)
        if option_level < 0:
            data = self._blur(data,option_level)
        
        return data
    
    
    def bit24(self, data, options={}):
        option_level = options["level"]
        
        if option_level > 0:
            data = self._sharp(data,option_level)
        if option_level < 0:
            data = self._blur(data,option_level)
        
        return data
    

    def _sharp(self, data, level):
        kernel = Kernel.sharp(level)
        
        result = cv2.filter2D(data, ddepth=-1, kernel=kernel)
        result = result.astype(data.dtype)

        return result

    def _blur(self, data, level):
        kernel = Kernel.blur(level)

        result = cv2.filter2D(data, ddepth=-1, kernel=kernel)
        result = result.astype(data.dtype)

        return result

class Kernel:
    @staticmethod
    def sharp(level):
        x = np.full((3,3),-1)
        x[1,1] = 9+level-1
        return x
        
    
    @staticmethod
    def blur(level):
        level = abs(level)*2
        return np.ones( (level,level) ) / (level*level)
    
'''
def sharp_blur(data, options={}):
    option_level = options["level"]1
    
    if option_level > 0:
        data = sharp(data,option_level)
    if option_level < 0:
        data = blur(data,option_level)
    
    return data
    
def sharp(data, level):
    kernel = Kernel.sharp(level)
    
    result = cv2.filter2D(data, ddepth=-1, kernel=kernel)
    result = result.astype(data.dtype)

    return result

def blur(data, level):
    kernel = Kernel.blur(level)

    result = cv2.filter2D(data, ddepth=-1, kernel=kernel)
    result = result.astype(data.dtype)

    return result
'''