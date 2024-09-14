'''
Given two binary strings a and b, return their sum as a binary string.
Example 1: Input: a = "11", b = "1"
Output: "100"
Example 2: Input: a = "1010", b = "1011"
Output: "10101"
'''

def add_binary(a, b):

	a = int(a, 2)
	b = int(b, 2)
	
	sum =  a+b
	
	return bin(sum)[2:]
	
print(add_binary('11', '1'))
print(add_binary('1010', '1011'))
