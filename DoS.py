from ctypes import *

if __name__ == "__main__":
	print(c_double.from_param(1e300))
