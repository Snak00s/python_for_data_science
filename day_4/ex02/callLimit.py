def callLimit(limit: int):
    """CallLimit init"""
    count = 0

    def callLimiter(function):
        """Function store"""
        def limit_function(*args: any, **kwds: any):
            """Limitation using limit"""
            nonlocal limit
            if (count < limit):
                function()
            else:
                print("Error: ", function, "call too many times")
            limit -= 1
            return
        return limit_function
    return callLimiter
