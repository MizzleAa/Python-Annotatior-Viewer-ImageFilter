from library.utils.header import *
from library.utils.abstract import AbstractBit

class Contrast(AbstractBit):
    
    def bit8(self, data, options={}):
        level = options["level"]
        max_data = np.iinfo(data.dtype).max
        min_data = np.iinfo(data.dtype).min
        middle = (max_data + min_data) / 2
        result = np.clip( (data)*(1 + level/10), min_data, max_data)
        result = result.astype(data.dtype)
        return result

    def bit16(self, data, options={}):
        level = options["level"]
        max_data = np.iinfo(data.dtype).max
        min_data = np.iinfo(data.dtype).min
        middle = (max_data + min_data) / 2
        result = np.clip( (data)*(1 + level/10), min_data, max_data)
        result = result.astype(data.dtype)
        return result

    def bit24(self, data, options={}):
        level = options["level"]
        max_data = np.iinfo(data.dtype).max
        min_data = np.iinfo(data.dtype).min
        middle = (max_data + min_data) / 2
        result = np.clip( (data)*(1 + level/10), min_data, max_data)
        result = result.astype(data.dtype)
        return result


'''
def contrast(data, options={}):
    level = options["level"]
    max_data = np.iinfo(data.dtype).max
    min_data = np.iinfo(data.dtype).min
    middle = (max_data + min_data) / 2
    result = np.clip( (data)*(1 + level/10), min_data, max_data)
    result = result.astype(data.dtype)
    return result
'''