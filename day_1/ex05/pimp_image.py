import numpy as np


def ft_invert(array) -> np.array:
    """
        Inverts the color of the image received.
    """
    try:
        assert type(array).__name__ == "np.array"
    except AssertionError:
        print("Invalid array")
        return []
    draw = np.copy(255 - array)
    return draw


def ft_red(array) -> np.array:
    """
        Apply red filter on the image array and return the result.
    """
    try:
        assert type(array).__name__ == "np.array"
    except AssertionError:
        print("Invalid array")
        return []
    draw = np.copy(array)
    for lines in draw:
        for rgb in lines:
            rgb[1] = 0
            rgb[2] = 0
    return draw


def ft_green(array) -> np.array:
    """
        Apply green filter on the image array and return the result.
    """
    try:
        assert type(array).__name__ == "np.array"
    except AssertionError:
        print("Invalid array")
        return []
    draw = np.copy(array)
    for lines in draw:
        for rgb in lines:
            rgb[0] = 0
            rgb[2] = 0
    return draw


def ft_blue(array) -> np.array:
    """
        Apply blue filter on the image array and return the result.
    """
    try:
        assert type(array).__name__ == "np.array"
    except AssertionError:
        print("Invalid array")
        return []
    draw = np.copy(array)
    for lines in draw:
        for rgb in lines:
            rgb[0] = 0
            rgb[1] = 0
    return draw


def ft_grey(array) -> np.ndarray:
    """
        Grayscale the image array and return the result.
    """
    try:
        assert type(array).__name__ == "np.array"
    except AssertionError:
        print("Invalid array")
        return []
    draw = np.copy(array)
    for i in range(len(draw)):
        for j in range(len(draw[i])):
            grey = 0
            if (draw[i][j][0] > 0):
                grey = np.sum([grey, 0.1140 / (1 / draw[i][j][0])])
            if (draw[i][j][1] > 0):
                grey = np.sum([grey, 0.5870 / (1 / draw[i][j][1])])
            if (draw[i][j][2] > 0):
                grey = np.sum([grey, 0.2989 / (1 / draw[i][j][2])])
            draw[i][j][0] = draw[i][j][1] = draw[i][j][2] = grey
    return draw
