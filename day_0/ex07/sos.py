import sys

NESTED_MORS = {" ": "/ ",
               "A": ".- ",
               "B": "-... ",
               "C": "-.-. ",
               "D": "-.. ",
               "E": ". ",
               "F": "..-. ",
               "G": "--. ",
               "H": ".... ",
               "I": ".. ",
               "J": ".--- ",
               "K": "-.- ",
               "L": ".-.. ",
               "M": "-- ",
               "N": "-. ",
               "O": "--- ",
               "P": ".--. ",
               "Q": "--.- ",
               "R": ".-. ",
               "S": "... ",
               "T": "- ",
               "U": "..- ",
               "V": "...- ",
               "W": ".-- ",
               "X": "-..- ",
               "Y": "-.-- ",
               "Z": "--.. ",
               "1": ".---- ",
               "2": "..--- ",
               "3": "...-- ",
               "4": "....- ",
               "5": "..... ",
               "6": "-.... ",
               "7": "--... ",
               "8": "---.. ",
               "9": "----. ",
               "0": "----- "}


def validstr(string: str) -> bool:
    for x in string:
        if (x.isalnum() is False and x.isspace() is False):
            return False
    return True


def main():
    try:
        assert len(sys.argv) == 2
        assert validstr(sys.argv[1]) is True
    except AssertionError:
        print("AssertError: the argument are bad")
        exit(1)

    retstr = ""
    for x in sys.argv[1]:
        retstr += NESTED_MORS[x.capitalize()]
    print(retstr)
    return


if __name__ == "__main__":
    main.__doc__ = "Display the sums of the upper-case, lower-case," \
        "punctuation, digit and spaces of the string."
    main()
