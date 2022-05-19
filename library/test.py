from library.utils.header import *
from library.utils.io import * 

def police_load():
    load_file_name="./sample/input/police8.png"

    load_options={
        "file_name":load_file_name,
        "dtype":np.uint8
    }
    image = load_image(load_options)
    return image

def police_save(image, options={}):
    file_name = options["file_name"]
    
    save_file_name=f"./sample/output/police8_{file_name}.png"

    if os.path.isfile(save_file_name):
        os.remove(save_file_name)
    
    dtype = image.dtype
    
    save_options={
        "file_name":save_file_name,
        "dtype":dtype,
        "start_pixel":np.iinfo(dtype).min,
        "end_pixel":np.iinfo(dtype).max
    }    
    #print(save_options)
    save_image(image, save_options)

    return save_file_name

def container_load():
    load_file_name="./sample/input/container.png"

    load_options={
        "file_name":load_file_name,
        "dtype":np.uint16
    }
    image = load_image(load_options)
    return image

def container_save(image, options={}):
    file_name = options["file_name"]
    
    save_file_name=f"./sample/output/container_{file_name}.png"
    if os.path.isfile(save_file_name):
        os.remove(save_file_name)
    
    dtype = image.dtype
    
    save_options={
        "file_name":save_file_name,
        "dtype":dtype,
        "start_pixel":np.iinfo(dtype).min,
        "end_pixel":np.iinfo(dtype).max
    }    
    #print(save_options)
    save_image(image, save_options)
    
    return save_file_name



def cow_load():
    load_file_name="./sample/input/cow.jpg"

    load_options={
        "file_name":load_file_name,
        "dtype":np.uint8
    }
    image = load_image(load_options)
    return image

def cow_save(image, options={}):
    file_name = options["file_name"]
    
    save_file_name=f"./sample/output/cow_{file_name}.png"

    if os.path.isfile(save_file_name):
        os.remove(save_file_name)
    
    dtype = image.dtype
    
    save_options={
        "file_name":save_file_name,
        "dtype":dtype,
        "start_pixel":np.iinfo(dtype).min,
        "end_pixel":np.iinfo(dtype).max
    }    
    #print(save_options)
    save_image(image, save_options)

    return save_file_name