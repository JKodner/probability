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
	"""Returns a list with the length of the 'length' parameter. The list's contents are of the
	keys for the **kwargs parameters. The amount of times each item appears are in the list, is
	the number of the item's key. Therefore, the item's probability of appearing in the list
	is: item's key/list's length.\n
	If the amount of items in the list is less than the list's length, the remaining contents
	are replaced with the 'None' keyword."""
	lst = []
	for i in kwargs.values():
		if not isinstance(i, int):
			raise ValueError("**Kwarg value is not int.")
	for i in kwargs.keys():
		for x in range(kwargs[i]):
			lst.append(i)
	for i in range(length - len(lst)):
		lst.append(None)
	return lst

def get_prob(key, lst):
	"""Returns the Probability of the 'key' parameter being in the inputed 'lst' parameter.
	Note: Returns a Fraction object from the 'fractions' module.\n
	If the key is not in the list, a 0/1 fraction is returned."""
	from fractions import Fraction
	count = 0
	for i in lst:
		if i == key:
			count += 1
	return Fraction(count, len(lst))

def odds(key, lst):
	"""Returns the Odds of the 'key' parameter in the inputed 'lst' parameter.
	Note: Returns a Fraction object from the 'fractions' module.\n
	If the key is not in the list, a 0/1 fraction is returned."""
	from fractions import Fraction
	success = 0
	failure = 0
	for i in lst:
		if i == key:
			success += 1
		else:
			failure += 1
	return Fraction(success, failure)



