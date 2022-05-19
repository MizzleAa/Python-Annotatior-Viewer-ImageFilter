from library.utils.header import *

class AbstractFilter(metaclass=ABCMeta):
    @abstractmethod
    def bright_dark(self):
        pass
    
    @abstractmethod
    def sharp_blur(self):
        pass
    
    @abstractmethod
    def reverse(self):
        pass
    
    @abstractmethod
    def roi(self):
        pass

    @abstractmethod
    def contrast(self):
        pass
    
class AbstractBit(metaclass=ABCMeta):
    
    @abstractmethod
    def bit8(self):
        pass
    
    @abstractmethod
    def bit16(self):
        pass
    
    @abstractmethod
    def bit24(self):
        pass
        