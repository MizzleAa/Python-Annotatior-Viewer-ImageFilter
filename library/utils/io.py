from library.utils.header import *

def cv_load_image(options):
    '''
    options = {
        "file_name": {file_name},
    }
    '''
    file_name = options["file_name"]
    
    image_array = np.fromfile(file_name, np.uint8)
    result = cv2.imdecode(image_array, -1)

    print(f"load image dtype={result.dtype} shape={result.shape}")

    return result

def cv_save_image(data, options):
    '''
    options = {
        "file_name": {file_name},
    }
    '''
    file_name = options["file_name"]
    dtype = options["dtype"]
    start_pixel = options["start_pixel"]
    end_pixel = options["end_pixel"]

    extension = os.path.splitext(file_name)[1]
    data = np.asarray(
        np.clip(data, start_pixel, end_pixel), dtype=dtype
    )
    result, encoded_img = cv2.imencode(extension, data)

    if result: 
        with open(file_name, mode="w+b") as f: 
            encoded_img.tofile(f)
    
    
def load_image(options):
    '''
    options = {
        "file_name": {file_name},
        "dtype": {dtype}
    }
    '''
    file_name = options["file_name"]
    dtype = options["dtype"]

    img = Image.open(file_name)
    img.load()
    
    data = np.asarray(img, dtype=dtype)
    return data

def save_image(data, options):
    '''
    options = {
        "file_name": {file_name},
        "dtype": {dtype},
        "start_pixel": {start_pixel},
        "end_pixel": {end_pixel}
    }
    '''
    file_name = options["file_name"]
    dtype = options["dtype"]
    start_pixel = options["start_pixel"]
    end_pixel = options["end_pixel"]

    img = Image.fromarray(
        np.asarray(
            np.clip(data, start_pixel, end_pixel), dtype=dtype
        )
    )
    img.save(file_name)

def save_raw(data, options):
    '''
    options = {
        "file_name": {file_name},
    }
    '''
    file_name = options["file_name"]

    data = data.flatten()
    myfmt = 'f' * len(data)
    file = open(file_name, "wb")
    binary = struct.pack(myfmt, *data)
    file.write(binary)
    file.close()
