import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI for the given arrays and return the result
    """

    try:
        assert (type(height).__name__ == "list") \
            and (type(weight).__name__ == "list")
        assert len(height) == len(weight)
    except AssertionError:
        print("Lists have not the same size")
        return []

    for x in range(len(height)):
        typ_name = type(height[x]).__name__
        if (typ_name != "float") and (typ_name != "int"):
            print("Wrong type in height list")
            return []
        typ_name = type(weight[x]).__name__
        if (typ_name != "float") and (typ_name != "int"):
            print("Wrong type in weight list")
            return []

    return [float(weight[x] / np.pow(height[x], 2))
            for x in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check BMI limit
    """
    try:
        assert (type(bmi).__name__ == "list") \
            and (type(limit).__name__ == "int")
    except AssertionError:
        print("Invalid argument")
        return []
    if len(bmi) == 0:
        return []
    return [x < limit for x in bmi]
