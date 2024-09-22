'''
Given a string s, reverse the order of characters in each word within 
a sentence while still preserving whitespace and initial word order.
'''

def reverseWords(s):
	reverse_words = []
	words = s.split()
	for word in words:
		reverse_words += [word[::-1]]
	return ' '.join(reverse_words)
	
s = "Let's take LeetCode contest"
print(reverseWords(s))
