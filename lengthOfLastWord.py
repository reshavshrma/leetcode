'''
Given a string s consisting of words and spaces, return 
the length of the last word in the string. A word is a maximal 
substring onsisting of non-space characters only.
 '''
 
def lengthOfLastWord(s):
	words = s.split()
	if words:
		return len(words[-1])
	else:
		return 0

print(lengthOfLastWord("Hello World"))
