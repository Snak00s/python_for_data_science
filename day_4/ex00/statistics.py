import numpy as np

def mean(nbr_list: list, display=False) -> float:
    try:
        assert len(nbr_list) != 0
    except AssertionError:
        print("ERROR")
        return
    ret = 0
    for x in nbr_list:
        ret += x
    ret /= len(nbr_list)
    if display is True:
        print("mean :", ret)
    return ret

def median(nbr_list: list, display=False) -> float:
    try:
        assert len(nbr_list) != 0
    except AssertionError:
        print("ERROR")
        return
    nbr_list = sorted(nbr_list)
    list_len = len(nbr_list)
    med = 0
    if list_len % 2 == 0:
        med = (nbr_list[int(list_len / 2) - 1]
               + nbr_list[int(list_len / 2)]) / 2
    else:
        med = nbr_list[int(list_len / 2)]
    if display is True:
        print("median :", med)
    return med

def quartile(nbr_list: list, display=False) -> list:
    try:
        assert len(nbr_list) != 0
    except AssertionError:
        print("ERROR")
        return
    nbr_list = sorted(nbr_list)
    list_len = len(nbr_list) - 1
    q1 = float(nbr_list[int((list_len + 3) / 4)])
    q2 = float(nbr_list[int((3 * list_len + 1) / 4)])
    if display is True:
        print("quartile :", [q1, q2])
    return [q1, q2]

def std(nbr_list: list, display=False) -> float:
    try:
        assert len(nbr_list) != 0
    except AssertionError:
        print("ERROR")
        return
    list_len = len(nbr_list)
    list_mean = mean(nbr_list)
    ret = 0
    for x in nbr_list:
        ret += float(x - list_mean) ** 2
    ret /= list_len
    ret **= 0.5
    if display is True:
        print("std :", ret)
    return ret

def variance(nbr_list: list, display=False) -> float:
    try:
        assert len(nbr_list) != 0
    except AssertionError:
        print("ERROR")
        return
    list_len = len(nbr_list)
    list_mean = mean(nbr_list)
    ret = 0
    for x in nbr_list:
        ret += float(x - list_mean) ** 2
    ret /= list_len
    if display is True:
        print("var :", ret)
    return ret



def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        for x in args:
            assert (type(x) is int) or (type(x) is float)
    except AssertionError:
        print("ERROR")
        return
    nbr_list = list(args)
    for task in kwargs:
        match kwargs[task]:
            case 'mean':
                mean(nbr_list, True)
            case 'median':
                median(nbr_list, True)
            case 'quartile':
                quartile(nbr_list, True)
            case 'std':
                std(nbr_list, True)
            case 'var':
                variance(nbr_list, True)
    return

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")