'''
Given a string s, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s):
	l, r = 0, 0
	max_length = 0
	
	while r < len(s):
		while s[r] in s[l:r]:
			l += 1
		max_length = max(r-l+1, max_length)
		r += 1
	return max_length 

print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))	
