import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    "Slice family list into a new list that start from start to end"
    if (type(family).__name__ != "list"):
        print("family is not a list")
        return []
    if (type(start).__name__ != "int"):
        print("start is not a int")
        return []
    if (type(end).__name__ != "int"):
        print("family is not a int")
        return []
    if len(family) != 0:
        ref_len = len(family[0])
        for x in family:
            if len(x) != ref_len:
                print("family entry are not all the same size")
                return []
    f_len = len(family)
    print(f"My shape is : ({f_len}, {0 if f_len == 0 else len(family[0])})")
    sli = [] if f_len == 0 \
        else [family[x] for x in range(np.abs(start), np.abs(end))]
    s_len = len(sli)
    print(f"My new shape is : ({s_len}, {0 if s_len == 0 else len(sli[0])})")
    return sli
