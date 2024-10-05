'''
Given a binary string s, return the number of non-empty substrings 
that have the same number of 0's and 1's, and all the 0's and all 
the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.
'''


def countBinarySubstrings(s):
	count = 0
	prev = 0
	curr = 1
	
	for i in range(1, len(s)):
		if s[i] == s[i-1]:
			curr += 1
		else:
			count += min(prev, curr)
			prev = curr
			curr = 1
	count += min(prev, curr)
	return count

print(countBinarySubstrings("00110011"))
print(countBinarySubstrings("10101"))
