'''
Given an integer num, repeatedly add all its digits 
until the result has only one digit, and return it. 
'''

def addDigits(num):
	
	while num >= 10:
		l = []
		num = str(num)
		for digits in num:
			l.append(int(digits))
		num = sum(l)
		
	return num
	
print(addDigits(38))
print(addDigits(0))
