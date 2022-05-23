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
        
        data = image_filters.bit16.bright_dark(image,  options={"level":-3})
        save_file_name = container_save(data, options={"file_name":"dark"})
        
        assert check_file(save_file_name) == True

        image = image_filters.bit16.bright_dark(image,  options={"level":3})
        save_file_name = container_save(image, options={"file_name":"bright"})
        
        assert check_file(save_file_name) == True

    def test_container_sharp_blur(self, image_filters):
        image = container_load()
        
        data = image_filters.bit16.sharp_blur(image,  options={"level":-1})
        save_file_name = container_save(data, options={"file_name":"sharp_blur"})
        
        assert check_file(save_file_name) == True

        data = image_filters.bit16.sharp_blur(image,  options={"level":+1})
        save_file_name = container_save(data, options={"file_name":"sharp_blur"})
        
        assert check_file(save_file_name) == True


    def test_container_contrast(self, image_filters):
        image = container_load()
        
        data = image_filters.bit16.contrast(image,  options={"level":5})
        save_file_name = container_save(data, options={"file_name":"contrast"})
        
        assert check_file(save_file_name) == True

    def test_container_reverse(self, image_filters):
        image = container_load()
        
        data = image_filters.bit16.reverse(image)
        save_file_name = container_save(data, options={"file_name":"reverse"})
        assert check_file(save_file_name) == True

    def test_container_roi(self, image_filters):
        image = container_load()

        image = image_filters.bit16.roi(image, options={"roi":[0,0,-1,-1]})
        save_file_name = container_save(image, options={"file_name":"roi"})

        assert check_file(save_file_name) == True

class Test8BitPolice:
    def test_police_bright_dark(self, image_filters):
        image = police_load()
        
        data = image_filters.bit8.bright_dark(image,  options={"level":-1})
        save_file_name = police_save(data, options={"file_name":"dark"})
        
        assert check_file(save_file_name) == True

        data = image_filters.bit8.bright_dark(image,  options={"level":1})
        save_file_name = police_save(data, options={"file_name":"bright"})
        
        assert check_file(save_file_name) == True

    def test_police_sharp_blur(self, image_filters):
        image = police_load()
        
        data = image_filters.bit8.sharp_blur(image,  options={"level":-1})
        save_file_name = police_save(data, options={"file_name":"blur"})
        
        assert check_file(save_file_name) == True

        data = image_filters.bit8.sharp_blur(image,  options={"level":1})
        save_file_name = police_save(data, options={"file_name":"sharp"})
        
        assert check_file(save_file_name) == True

    def test_police_contrast(self, image_filters):
        image = police_load()
        
        data = image_filters.bit8.contrast(image,  options={"level":5})
        save_file_name = police_save(data, options={"file_name":"contrast"})

        assert check_file(save_file_name) == True

    def test_police_reverse(self, image_filters):
        image = police_load()
        
        data = image_filters.bit8.reverse(image)
        save_file_name = police_save(data, options={"file_name":"reverse"})

        assert check_file(save_file_name) == True

    def test_police_roi(self, image_filters):
        image = police_load()
        
        data = image_filters.bit8.roi(image, options={"roi":[0,0,-1,-1]})
        save_file_name = police_save(data, options={"file_name":"roi"})
        
        assert check_file(save_file_name) == True

class Test24BitCow:
    def test_cow_bright_dark(self, image_filters):
        image = cow_load()

        data = image_filters.bit24.bright_dark(image,  options={"level":-1})
        save_file_name = cow_save(data, options={"file_name":"dark"})

        assert check_file(save_file_name) == True

        data = image_filters.bit24.bright_dark(image,  options={"level":1})
        save_file_name = cow_save(data, options={"file_name":"bright"})

        assert check_file(save_file_name) == True

    def test_cow_sharp_blur(self, image_filters):
        image = cow_load()
        
        data = image_filters.bit24.sharp_blur(image,  options={"level":-1})
        save_file_name = cow_save(data, options={"file_name":"blur"})
        
        assert check_file(save_file_name) == True
    
        data = image_filters.bit24.sharp_blur(image,  options={"level":1})
        save_file_name = cow_save(data, options={"file_name":"sharp"})
        
        assert check_file(save_file_name) == True
    
    def test_cow_contrast(self, image_filters):
        image = cow_load()
        
        image = image_filters.bit24.contrast(image,  options={"level":5})
        save_file_name = cow_save(image, options={"file_name":"contrast"})

        assert check_file(save_file_name) == True
        
    def test_cow_reverse(self, image_filters):
        image = cow_load()
        
        image = image_filters.bit24.reverse(image)
        save_file_name = cow_save(image, options={"file_name":"reverse"})
        assert check_file(save_file_name) == True
        
    def test_cow_roi(self, image_filters):
        image = cow_load()
        
        image = image_filters.bit24.roi(image, options={"roi":[0,0,-1,-1]})
        save_file_name = cow_save(image, options={"file_name":"roi"})
        assert check_file(save_file_name) == True