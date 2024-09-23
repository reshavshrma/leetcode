'''
Given a string of English letters s, return the greatest English 
letter which occurs as both a lowercase and uppercase letter in s.
The returned letter should be in uppercase. If no such letter exists, 
return an empty string. An English letter b is greater than another 
letter a if b appears after a in the English alphabet.
'''

def greatestLetter(self, s):
	greatest = ''
	for i in s:
		if i.lower() in s and i.upper() in s:
			greatest = max(greatest, i.upper())
	return greatest
	
s = "lEeTcOdE"
print(greatestLetter(s))
