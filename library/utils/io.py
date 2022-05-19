from library.utils.header import *

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
