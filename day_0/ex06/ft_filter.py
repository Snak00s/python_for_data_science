
def myFunc(x):
    if x < 18:
        return False
    else:
        return True


def ft_filter(func, object: any):
    "Return an iterator yielding those items of iterable for which func(item)\
 is true. If function is None, return the items that are true."

    newlist = [x for x in object if func(x) is True]
    return newlist.__iter__()
