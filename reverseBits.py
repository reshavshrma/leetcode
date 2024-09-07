'''
Reverse bits of a given 32 bits unsigned integer.
'''

def reverseBits(n):
	
	#convert integer into binary string
	str_n = bin(n)[2:].zfill(32)
	
	#reverse the binary string 
	reversed_n = str_n[::-1]
	
	#return the reversed binary string as integer
	return int(reversed_n, 2)
	
print(reverseBits(0b00000010100101000001111010011100))
print(reverseBits(0b11111111111111111111111111111101))
