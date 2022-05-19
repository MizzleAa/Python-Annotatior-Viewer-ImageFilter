from library.test import *
from library.asserts.valid import *
from library.image_filter import ImageFilter

import pytest

@pytest.fixture
def image_filters():
    image_filter = ImageFilter()
    return image_filter

class Test16BitContainer:
    def test_container_bright_dark(self, image_filters):
        image = container_load()
        
        #algorithm start
        #for i in range(-10,10,1):
        image = image_filters.bit16.bright_dark(image,  options={"level":0})
        #algorithm end
        save_file_name = container_save(image, options={"file_name":"bright_dark"})
        #test
        assert check_file(save_file_name) == True

    def test_container_sharp_blur(self, image_filters):
        image = container_load()
        
        #algorithm start
        # for i in range(-10,10,1):
        image = image_filters.bit16.sharp_blur(image,  options={"level":0})
        #algorithm end
        save_file_name = container_save(image, options={"file_name":"sharp_blur"})
        #test
        assert check_file(save_file_name) == True

    def test_container_contrast(self, image_filters):
        image = container_load()
        
        image = image_filters.bit16.contrast(image,  options={"level":5})
        #algorithm end
        save_file_name = container_save(image, options={"file_name":"contrast"})
        #test
        assert check_file(save_file_name) == True

    def test_container_reverse(self, image_filters):
        image = container_load()
        
        image = image_filters.bit16.reverse(image)
        #algorithm end
        save_file_name = container_save(image, options={"file_name":"reverse"})
        #test
        assert check_file(save_file_name) == True

    def test_container_roi(self, image_filters):
        image = container_load()
        
        image = image_filters.bit16.roi(image, options={"roi":[0,0,100,100]})
        #algorithm end
        save_file_name = container_save(image, options={"file_name":"roi"})
        #test
        assert check_file(save_file_name) == True

class Test8BitPolice:
    def test_police_bright_dark(self, image_filters):
        image = police_load()
        
        #algorithm start
        #for i in range(-10,10,1):
        image = image_filters.bit8.bright_dark(image,  options={"level":0})
        #algorithm end
        save_file_name = police_save(image, options={"file_name":"bright_dark"})
        #test
        assert check_file(save_file_name) == True

    def test_police_sharp_blur(self, image_filters):
        image = police_load()
        
        #algorithm start
        # for i in range(-10,10,1):
        image = image_filters.bit8.sharp_blur(image,  options={"level":0})
        #algorithm end
        save_file_name = police_save(image, options={"file_name":"sharp_blur"})
        #test
        assert check_file(save_file_name) == True

    def test_police_contrast(self, image_filters):
        image = police_load()
        
        image = image_filters.bit8.contrast(image,  options={"level":5})
        #algorithm end
        save_file_name = police_save(image, options={"file_name":"contrast"})
        #test
        assert check_file(save_file_name) == True

    def test_police_reverse(self, image_filters):
        image = police_load()
        
        image = image_filters.bit8.reverse(image)
        #algorithm end
        save_file_name = police_save(image, options={"file_name":"reverse"})
        #test
        assert check_file(save_file_name) == True

    def test_police_roi(self, image_filters):
        image = police_load()
        
        image = image_filters.bit8.roi(image, options={"roi":[0,0,100,100]})
        #algorithm end
        save_file_name = police_save(image, options={"file_name":"roi"})
        #test
        assert check_file(save_file_name) == True

class Test24BitCow:
    def test_cow_bright_dark(self, image_filters):
        image = cow_load()
        
        #algorithm start
        #for i in range(-10,10,1):
        image = image_filters.bit24.bright_dark(image,  options={"level":5})
        #algorithm end
        save_file_name = cow_save(image, options={"file_name":"bright_dark"})
        #test
        assert check_file(save_file_name) == True

    def test_cow_sharp_blur(self, image_filters):
        image = cow_load()
        
        #algorithm start
        # for i in range(-10,10,1):
        image = image_filters.bit24.sharp_blur(image,  options={"level":5})
        #algorithm end
        save_file_name = cow_save(image, options={"file_name":"sharp_blur"})
        #test
        assert check_file(save_file_name) == True
    
    def test_cow_contrast(self, image_filters):
        image = cow_load()
        
        image = image_filters.bit24.contrast(image,  options={"level":-4})
        #algorithm end
        save_file_name = cow_save(image, options={"file_name":"contrast"})
        #test
        assert check_file(save_file_name) == True
        
    def test_cow_reverse(self, image_filters):
        image = cow_load()
        
        image = image_filters.bit24.reverse(image)
        #algorithm end
        save_file_name = cow_save(image, options={"file_name":"reverse"})
        #test
        assert check_file(save_file_name) == True
        
    def test_cow_roi(self, image_filters):
        image = cow_load()
        
        image = image_filters.bit24.roi(image, options={"roi":[0,0,100,100]})
        #algorithm end
        save_file_name = cow_save(image, options={"file_name":"roi"})
        #test
        assert check_file(save_file_name) == True