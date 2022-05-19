from library.utils.header import *
from library.utils.abstract import AbstractBit

class Reverse(AbstractBit):
    def bit8(self, data, options={}):
        max_data = np.iinfo(data.dtype).max
        result = max_data - data
        return result
    
    def bit16(self, data, options={}):
        max_data = np.iinfo(data.dtype).max
        result = max_data - data
        return result
    
    def bit24(self, data, options={}):
        max_data = np.iinfo(data.dtype).max
        result = max_data - data
        return result
    
'''
def reverse(data, options={}):
    max_value = np.iinfo(data.dtype).max
    result = max_value - data
    return result
'''