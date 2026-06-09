def all_thing_is_obj(object: any) -> int:
	if (type(object).__name__ == "str"):
		name = str(object)
		print(name, "is in the kitchen", ':', type(object))
	else:
		print(type(object).__name__.capitalize(), ':', type(object))
	return(42)