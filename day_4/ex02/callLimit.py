def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal limit
            if (count < limit):
                function()
            else:
                print("Error: ", function, "call too many times")
            limit -= 1
            return
        return limit_function
    return callLimiter
