'''
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits it has (also known as the Hamming weight).
Example 1: Input: n = 11 => Output: 3
'''

def no_of_1_bits(n):
	bin_n = bin(n)[2:]
	
	count = 0
	for index in bin_n:
		if index == '1':
			count += 1
	return count
	
print(no_of_1_bits(128))
print(no_of_1_bits(11))
