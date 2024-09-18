'''
Write a function that takes the binary representation of
a positive integer and returns the number of set bits
it has (also known as the Hamming weight).
'''

def hammingWeight(n):
	bin_n = bin(n)[2:]
	count = 0
	for index in bin_n:
		if index == '1':
			count += 1
	return count
	
print(hammingWeight(11))
