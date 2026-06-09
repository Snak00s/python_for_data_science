
# def is_capitalize(string: str):
# 	return (string[0].isupper())

def ft_filter(object: any, func) -> bool:
	newlist = [x for x in object if func(x) is True]
	return newlist

# test = ["yo", "Noway", "Feur", "no", "issou"]

# print(ft_filter(test, is_capitalize))