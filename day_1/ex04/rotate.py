from load_image import ft_load
import sys
import numpy as np
import matplotlib.pyplot as plt


def slice_img(img_arr: np.array) -> np.array:
    """Slice the image array into a 2D, 1 value array"""
    try:
        assert type(img_arr).__name__ == "ndarray"
        arr_sh = np.shape(img_arr)
        assert (len(arr_sh) == 3) and (arr_sh[2] == 3)
    except AssertionError:
        print("Invali array")
        return None
    return (0.2126 * img_arr[:, :, 0:1]
            + 0.7152 * img_arr[:, :, 1:2]
            + 0.0722 * img_arr[:, :, 2:3]).astype(int)


def zoom_img(img_arr: np.array,
             x_start: int, x_end: int, y_start: int, y_end: int) -> np.array:
    """Zoom inside the image by selecting idx with x_start, ... y_end"""
    try:
        assert type(img_arr).__name__ == "ndarray"
        assert type(x_start).__name__ == "int"
        assert type(x_end).__name__ == "int"
        assert type(y_start).__name__ == "int"
        assert type(y_end).__name__ == "int"
    except AssertionError:
        print("Invalid array or value not int")
        return None
    return img_arr[y_start:y_end, x_start:x_end]


def zoom(img_arr: np.array) -> np.array:
    """
    Zoom inside the image by selecting idx with x_start, ... y_end
    """
    img_arr = slice_img(img_arr)
    if (type(img_arr).__name__ == "NoneType"):
        return False
    img_arr = zoom_img(img_arr, 450, 850, 100, 500)
    if (type(img_arr).__name__ == "NoneType"):
        return False
    img_sh = np.shape(img_arr)
    print(f"The shape of image is: {img_sh} or ({img_sh[0]}, {img_sh[1]})")
    print(img_arr)
    return img_arr


def transpose(img_arr: np.array):
    """
    Transpose the array
    """
    img_arr = img_arr[:, :, 0]
    img_sh = np.shape(img_arr)
    img_arr_t = np.array([np.array([int(x[y]) for x in img_arr])
                          for y in range(img_sh[1])])
    print("New shape after Transpose: ", np.shape(img_arr_t))
    print(img_arr_t)
    plt.imshow(img_arr_t, cmap="gray")
    plt.show()
    return


def main():
    try:
        assert len(sys.argv) == 2
    except AssertionError:
        print("Need exactly 1 argument")
        exit(1)
    img_arr = ft_load(sys.argv[1])
    img_arr = zoom(img_arr)
    transpose(img_arr)

    return


if __name__ == "__main__":
    main()
