import sys


def main():
    try:
        assert len(sys.argv) <= 2
    except AssertionError:
        print("AssertionError: more than one argument is provided")
        exit(0)
    string = 0
    if (len(sys.argv) == 2):
        string = sys.argv[1]
    else:
        try:
            string = input("What is the text to count?\n")
        except EOFError:
            print("EOFError: input is an EOF")
            exit(0)

    ll, ul, di, pm, sp = 0, 0, 0, 0, 0
    for c in string:
        if (c.isalpha() is True):
            if (c.islower() is True):
                ll += 1
            else:
                ul += 1
        elif (c.isdigit() is True):
            di += 1
        elif (c.isspace() is True):
            sp += 1
        else:
            pm += 1
    print("The text contain", len(string), "characters:")
    print(ul, "upper letters")
    print(ll, "lower letters")
    print(pm, "punctuation marks")
    print(sp, "spaces")
    print(di, "digits")
    return


if __name__ == "__main__":
    main.__doc__ = "Display the sums of the upper-case, lower-case," \
        "punctuation, digit and spaces of the string."
    main()
