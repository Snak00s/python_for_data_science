from PIL import Image as img
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        file = img.open(path)
    except IOError:
        print("Invalid image")
        return [[]]

    file_arr = np.array(file)
    return file_arr
