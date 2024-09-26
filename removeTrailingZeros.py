'''
Given a positive integer num represented as a string, 
return the integer num without trailing zeros as a string.
'''

def removeTrailingZeros(num):
	return num.rstrip('0')
	
print(removeTrailingZeros(num))
