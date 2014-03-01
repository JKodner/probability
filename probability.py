"""The Probability Module, made by Jacob Kodner"""

def factorial(n):
	"""Returns the Factorial of a number."""
	num = 1
	if not (isinstance(n, int) and n >= 0):
		raise ValueError("Parameter must be a positive integer")
	else:
		for i in range(1, n+1):
			num *= i
	return num

def permutation(n, r, rep=False):
	"""Returns the number of Permutations in a set.\n
	Three Parameters: 
	n = number of items
	r = number of those items
	rep = True if Repition is allowed, False if Repition is not allowed (default=False).\n
	Formula with No Repition: P(n,r) = n! / (n-r)!
	Formula with Repition: (n^r)!\n
	Note: Function does not return decimals. The numbers can be too big, and may cause
	Overflow Errors if converted to float."""
	if not (isinstance(n, int) and isinstance(r, int) and n >= 0 and r >= 0):
		raise ValueError("Parameters must be positive integers.")
	elif rep not in [True, False]:
		raise ValueError("Repition Parameter must be True or False")
	else:
		if rep == False:
			first = factorial(n)
			second = factorial(n-r)
		elif rep:
			first = factorial(n**r)
			second = 1
		return first / second

		

def combination(n, r, rep=False):
	"""Returns the number of Combinations in a set.\n
	Three Parameters: 
	n = number of items
	r = number of those items
	rep = True if Repition is allowed, False if Repition is not allowed (default=False).\n
	Formula with No Repition: C(n,r) = n! / r!(n-r)!
	Formula with Repition: C(n,r) = (n+r-1)! / r!(n-1)!\n
	Note: Function does not return decimals. The numbers can be too big, and may cause
	Overflow Errors if converted to float."""
	if not (isinstance(n, int) and isinstance(r, int) and n >= 0 and r >= 0):
		raise ValueError("Parameters must be positive integers.")
	elif rep not in [True, False]:
		raise ValueError("Repeition Parameter must be True or False.")
	else:
		if rep == False:
			first = factorial(n)
			second = factorial(r) * factorial(n-r)
		elif rep:
			first = factorial(n+r-1)
			second = factorial(r) * factorial(n-1)
		return first / second

def prob_list(length, **kwargs):
	lst = []
	for i in kwargs.keys():
		for x in range(kwargs[i]):
			lst.append(i)
	for i in range(length - len(lst)):
		lst.append(None)
	return lst

def get_prob(key, lst):
	from fractions import Fraction
	count = 0
	for i in lst:
		if i == key:
			count += 1
	return Fraction(count, len(lst))



