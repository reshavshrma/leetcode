'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''

def sqrt(n):
	a = 0
	
	while(a*a <= n):
		a += 1
	return a-1
	
print(sqrt(8))
print(sqrt(0))
print(sqrt(4))
print(sqrt(25))
