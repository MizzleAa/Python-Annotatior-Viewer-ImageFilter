
from library.image_filter import ImageFilter
from library.test import *

class Test16BitContainer:
    def __init__(self):
        self.image_filter = ImageFilter()
        
    def test_bright_dark(self):
        image = container_load()
        #algorithm start
        image = self.image_filter.bit16.bright_dark(image, options={"level":1})
        #algorithm end
        container_save(image, options={"file_name":"bright_dark"})

    def test_sharp_blur(self):
        image = container_load()
        #algorithm start
        image = self.image_filter.bit16.sharp_blur(image, options={"level":-3})
        #algorithm end
        container_save(image, options={"file_name":"sharp_blur"})
        
    def test_reverse(self):
        image = container_load()
        #algorithm start
        image = self.image_filter.bit16.reverse(image)
        #algorithm end
        container_save(image, options={"file_name":"reverse"})

    def test_roi(self):
        image = container_load()
        #algorithm start
        image = self.image_filter.bit16.roi(image, options={"roi":[0,0,5,5]})
        #algorithm end
        container_save(image, options={"file_name":"roi"})

    def test_contrast(self):
        image = container_load()
        #algorithm start
        image = self.image_filter.bit16.contrast(image, options={"level":0})
        #algorithm end
        container_save(image, options={"file_name":"contrast"})


class Test8BitPolice:
    def __init__(self):
        self.image_filter = ImageFilter()
        
    def test_bright_dark(self):
        image = police_load()
        #algorithm start
        image = self.image_filter.bit8.bright_dark(image, options={"level":1})
        #algorithm end
        police_save(image, options={"file_name":"bright_dark"})

    def test_sharp_blur(self):
        image = police_load()
        #algorithm start
        image = self.image_filter.bit8.sharp_blur(image, options={"level":-3})
        #algorithm end
        police_save(image, options={"file_name":"sharp_blur"})
        
    def test_reverse(self):
        image = police_load()
        #algorithm start
        image = self.image_filter.bit8.reverse(image)
        #algorithm end
        police_save(image, options={"file_name":"reverse"})

    def test_roi(self):
        image = police_load()
        #algorithm start
        image = self.image_filter.bit8.roi(image, options={"roi":[0,0,5,5]})
        #algorithm end
        police_save(image, options={"file_name":"roi"})

    def test_contrast(self):
        image = police_load()
        #algorithm start
        image = self.image_filter.bit8.contrast(image, options={"level":0})
        #algorithm end
        police_save(image, options={"file_name":"contrast"})

   
if __name__ == '__main__':
    test_8bit_police =  Test8BitPolice()
    test_8bit_police.test_bright_dark()
