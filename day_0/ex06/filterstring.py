import sys
from ft_filter import ft_filter


def filterstring(string: str, size: int) -> list:
    lst = string.split()

    retlst = list(ft_filter(lambda x: len(x) >= int(size), lst))
    return retlst


def main():
    try:
        assert len(sys.argv) == 3
    except AssertionError:
        print("AssertionError: more or less than 2 argument")
        exit(1)
    try:
        assert sys.argv[1].isprintable() is True
    except AssertionError:
        print("AssertionError: invalid string")
        exit(1)
    try:
        assert sys.argv[2].isnumeric() is True
    except AssertionError:
        print("AssertionError: invalid size")
        exit(1)

    print(filterstring(sys.argv[1], sys.argv[2]))

    return


if __name__ == "__main__":
    main.__doc__ = "Display the sums of the upper-case, lower-case," \
        "punctuation, digit and spaces of the string."
    main()
