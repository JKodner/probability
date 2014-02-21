def factorial(x):
	"""Returns the Factorial of a number."""
	num = 1
	if not isinstance(x, int):
		raise ValueError("Parameter must be an integer")
	else:
		for i in range(1, x+1):
			num *= i
	return num

