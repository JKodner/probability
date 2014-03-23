"""The Probability Module"""

__author__ = "Jacob Kodner (jake@kodner.net)"

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
	"""Returns the number of Permutations in a set.

	Three Parameters: 
	n = number of items
	r = number of those items
	rep = True if Repition is allowed, False if Repition is not allowed (default=False).

	Formula with No Repition: P(n,r) = n! / (n-r)!
	Formula with Repition: (n^r)!
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
	"""Returns the number of Combinations in a set.

	Three Parameters: 
	n = number of items
	r = number of those items
	rep = True if Repition is allowed, False if Repition is not allowed (default=False).

	Formula with No Repition: C(n,r) = n! / r!(n-r)!
	Formula with Repition: C(n,r) = (n+r-1)! / r!(n-1)!
	
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

def prob_list(**kwargs):
	"""The list's contents are of the keys for the **kwargs parameters. 

	The amount of times each item appears are in the list, is the number of the item's key. 
	Therefore, the item's probability of appearing in the list is: item's key/list's length.
	If the amount of items in the list is less than the list's length, the remaining contents
	are replaced with the 'None' keyword."""
	lst = []
	for i in kwargs.values():
		if not isinstance(i, int):
			raise ValueError("**Kwarg value is not int.")
	for i in kwargs.keys():
		for x in range(kwargs[i]):
			lst.append(i)
	return lst

def get_prob(key, lst, fract=True, notkey=False):
	"""Returns the Probability of the 'key' parameter being in the inputed 'lst' parameter.

	Note: If you want a Fraction object (from the fractions module) outputted, input the
	'fract' parameter as True (default). If not, input False, which will output a string. 
	Please note that Fraction objects are simplified, but the string versions are not.
	
	There is also a 'notkey' parameter. If notkey is equal to True, this function outputs the
	probability of the 'key' parameter not being in the 'lst' parameter. If it equals False
	(default), this function returns the probability of 'key' being in 'lst'."""
	if not isinstance(lst, list):
		raise ValueError("Lst parameter must be a list")
	elif notkey not in [True, False]:
		raise ValueError("Notkey parameter must be True or False")
	elif fract not in [True, False]:
		raise ValueError("Fract parameter must be True or False")
	count = 0
	for i in lst:
		if i == key:
			count += 1
	if fract == True:
		from fractions import Fraction
		if notkey:
			if count == 0:
				prob = Fraction(0, len(lst))
			else:
				prob = Fraction(len(lst) - count, len(lst))
		else:
			prob = Fraction(count, len(lst))
	elif fract == False:
		if notkey:
			if count == 0:
				prob = '0/%s' % len(lst)
			else:
				prob = '%s/%s' % (len(lst) - count, len(lst))
		else:
			prob = '%s/%s' % (count, len(lst))
	return prob

def get_prob_rand(key, lst, times, fract=True, notkey=False):
	"""Returns the Probability of the 'key' parameter being in the inputed 'lst' parameter.

	This function calculates the probability by randomly choosing the inputted list's contents
	and seeing if there is a match to the 'key' parameter. 

	The 'times' parameter is the number of times the function chooses a random content.

	The Fraction returned is: [ # of times found randomly / len(lst) ] * times

	Note: If you want a Fraction object (from the fractions module) outputted, input the
	'fract' parameter as True (default). If not, input False, which will output a string. 
	Please note that Fraction objects are simplified, but the string versions are not.
	
	There is also a 'notkey' parameter. If notkey is equal to True, this function outputs the
	probability of the 'key' parameter not being in the 'lst' parameter. If it equals False
	(default), this function returns the probability of 'key' being in 'lst'."""
	if not isinstance(lst, list):
		raise ValueError("Lst parameter must be a list")
	elif not isinstance(times, int) or times <= 0:
		raise ValueError("Times parameter must be a positive integer.")
	elif notkey not in [True, False]:
		raise ValueError("Notkey parameter must be True or False")
	elif fract not in [True, False]:
		raise ValueError("Fract parameter must be True or False")
	count = 0
	num = len(lst) * times
	if key in lst:
		from random import choice
		for x in range(len(lst)):
			for i in range(times):
				i = choice(lst)
				if i == key:
					count += 1
	if notkey:
		count = num - count
	if fract:
		from fractions import Fraction
		obj = Fraction(count, num)
	else:
		obj = "%s/%s" % (count, num)
	return obj

def odds(key, lst, notkey=False, fract=True):
	"""Returns the Odds of the 'key' parameter in the inputed 'lst' parameter.

	Note: If you want a Fraction object (from the fractions module) outputted, input the
	'fract' parameter as True (default). If not, input False, which will output a string. 
	Please note that Fraction objects are simplified, but the string versions are not."""
	from fractions import Fraction
	if fract not in [True, False]:
		raise ValueError("Fract parameter must be True or False")
	success = 0
	failure = 0
	for i in lst:
		if i == key:
			success += 1
		else:
			failure += 1
	if fract == True:
		from fractions import Fraction
		if notkey:
			prob = Fraction(failure, success)
		else:
			prob = Fraction(success, failure)
	elif fract == False:
		if notkey:
			prob = '%s/%s' % (failure, success)
		else:
			prob = '%s/%s' % (success, failure)
	return prob

def status(prob):
	"""Determines the chance of an event happening with a given probability.

	The possible outputs are: impossible, unlikely, even, likely, certain. 

	The inputted 'prob' value can be a Fraction object from the 'fractions' module, an integer, or
	in a string version."""
	if prob.__class__.__name__ == "Fraction":
		new_val = [prob.numerator, prob.denominator]
	elif isinstance(prob, str):
		from re import match
		patt = r'-?\d+(.\d+)? */ *-?\d+(.\d+)?'
		if not match(patt, prob):
			if match(r'-?\d+(.\d+)?', prob):
				new_val = [float(prob), 1]
			raise ValueError('Input is not Fraction')
		else:
			new_val = prob.split('/')
			new_val = map(lambda prob: prob.strip(), new_val)
			new_val = map(float, new_val)
	elif isinstance(prob, (int, float)) and prob >= 0:
		new_val = [float(prob), 1]
	else:
		raise ValueError('Input is not Fraction')
	div = new_val[0] / new_val[1]
	if 0 < div < 0.5:
		status = "unlikely"
	elif 0.5 < div < 1:
		status = "likely"
	elif div <= 0:
		status = "impossible"
	elif div == 0.5:
		status = "even"
	elif div >= 1:
		status = "certain"
	return status
