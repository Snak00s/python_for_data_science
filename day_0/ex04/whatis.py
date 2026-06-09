import sys

try:
	assert len(sys.argv) == 2
except AssertionError:
	print("AssertionError: more than one argument is provided")
	exit(0)

nbr = str()
if ((sys.argv[1])[0] == '-'):
	nbr = (sys.argv[1]).removeprefix('-')
elif ((sys.argv[1])[0] == '+'):
	nbr = (sys.argv[1]).removeprefix('+')
else:
	nbr = sys.argv[1]

try:
	assert (nbr.isnumeric() == True)
except AssertionError:
	print("AssertionError: argument is not an integer")
	exit(0)

nbr = int(nbr)

if (nbr % 2 == 0):
	print("I'm Even")
else:
	print("I'm Odd")