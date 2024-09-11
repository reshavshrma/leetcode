'''
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
'''

def isPowerOfFour(n):
	
	if n == 0:
		return False
		
	while n%4 == 0:
		n /= 4
	return n == True
	
print(isPowerOfFour(16))
print(isPowerOfFour(5))
print(isPowerOfFour(1))
