class calculator:
    """class that register an object and allow you to
    do operation on it"""
    def __init__(self, obj: object):
        """Init calculator"""
        self.vect = obj
        return

    def __add__(self, object) -> None:
        """add object to calculator object"""
        self.vect = type(self.vect)([x + object for x in self.vect])
        print(self.vect)
        return

    def __mul__(self, object) -> None:
        """mul object to calculator object"""
        self.vect = type(self.vect)([x * object for x in self.vect])
        print(self.vect)
        return

    def __sub__(self, object) -> None:
        """sub object to calculator object"""
        self.vect = type(self.vect)([x - object for x in self.vect])
        print(self.vect)
        return

    def __truediv__(self, object) -> None:
        """div object to calculator object"""
        try:
            1 / object
        except ZeroDivisionError:
            print("Error: Division by 0")
            return
        self.vect = type(self.vect)([x / object for x in self.vect])
        print(self.vect)
        return
