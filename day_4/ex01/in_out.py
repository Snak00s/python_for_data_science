def square(x: int | float) -> int | float:
    """Calculate the square"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Exponentiation of argument by himself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Init count"""
    count = 0

    def inner() -> float:
        """Apply the func on the number"""
        nonlocal count
        count += 1
        ret = x
        for _ in range(count):
            ret = function(ret)
        return ret
    return inner
