'''
Given a signed 32-bit integer x, return x with its digits reversed.
 If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

def reverseInteger(x):
	if x > -2**31:
		
		# convert integer into string
		new_x = str(x)
		
		# do reverse using slicing 
		if new_x[0] == '-':
			reverse_x = '-' + new_x[:0:-1]
		else:
			reverse_x = new_x[::-1]
		
		# again convert string into number 
		reversed_x = int(reverse_x)
		
		# now check if it is between unsigned integer or not
		if -2**31 <= reversed_x <= 2**31 - 1:
			return reversed_x
		else:
			return 0
		
#sample cases
print(reverseInteger(123))
print(reverseInteger(-321))
