from load_image import ft_load
import sys
import numpy as np
from PIL import Image as img
import matplotlib.pyplot as plt

# Clinear = 0.2126 R + 0.7152 G + 0.0722 B

def main():
	try:
		assert len(sys.argv) == 2
	except AssertionError:
		print("Need exactly 1 argument")
		exit(1)
	file = ft_load(sys.argv[1])
	if (file == []):
		exit(1)
	# print(file)
	
# your tests and your error handling
if __name__ == "__main__":
	main()