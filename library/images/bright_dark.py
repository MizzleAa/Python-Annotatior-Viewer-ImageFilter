from library.utils.header import *
from library.utils.abstract import AbstractBit

class BrightDark(AbstractBit):
    
    def bit8(self, data, options={}):
        option_level = options["level"] / 10
        data_max = np.iinfo(data.dtype).max
        data_min = np.iinfo(data.dtype).min
        
        float_data = data / data_max
        result = float_data + option_level
        result = result * data_max
        result[result > data_max] = data_max
        result[result < data_min] = data_min
        
        result= result.astype(data.dtype)
        return result
    
    def bit16(self, data, options={}):
        option_level = options["level"] / 10
        data_max = np.iinfo(data.dtype).max
        data_min = np.iinfo(data.dtype).min
        
        float_data = data / data_max
        result = float_data + option_level
        result = result * data_max
        result[result > data_max] = data_max
        result[result < data_min] = data_min
        
        result= result.astype(data.dtype)
        return result
    
    def bit24(self, data, options={}):
        option_level = options["level"] / 10
        data_max = np.iinfo(data.dtype).max
        data_min = np.iinfo(data.dtype).min
        
        float_data = data / data_max
        result = float_data + option_level
        result = result * data_max
        result[result > data_max] = data_max
        result[result < data_min] = data_min
        
        result= result.astype(data.dtype)
        return result
    

'''
def bright_dark(data, options={}):
    option_level = options["level"]
    data_max = np.iinfo(data.dtype).max
    data_min = np.iinfo(data.dtype).min
    
    float_data = data / data_max
    result = float_data + option_level
    result = result * data_max
    result[result > data_max] = data_max
    result[result < data_min] = data_min
    
    result= result.astype(data.dtype)
    return result
'''