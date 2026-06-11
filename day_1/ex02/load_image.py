from PIL import Image as img


def ft_load(path: str) -> list:
    try:
        file = img.open(path)
    except IOError:
        print("Invalid image")
        return []

    ret = []
    for x in range(file.width):
        for y in range(file.height):
            ret.append(list(file.getpixel([x, y])))
    print(f"The shape of image is: ({file.height}, {
        file.width}, {len(ret[0])})")
    file.close()
    return ret
