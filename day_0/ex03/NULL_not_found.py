def NULL_not_found(object: any) -> int:

	x = str()
	match type(object).__name__:
		case 'str':
			if (object != ""):
				print("Type not found")
				return (1)
			x = "Empty:"
		case 'float':
			if (object == object):
				print("Type not found")
				return (1)
			x = "Cheese:"
		case 'int':
			if (object != 0):
				print("Type not found")
				return (1)
			x = "Zero:"
		case 'bool':
			if (object != False):
				print("Type not found")
				return (1)
			x = "Fake:"
		case 'NoneType':
			x = 'None:'

	print(x, ValueError(object), type(object))
	return (0)