'''
Given a string s, find the first non-repeating character 
in it and return its index. If it does not exist, return -1.
'''
        
def firstUniqChar(s):
	char_count = {}
	
	for char in s:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	
	for index, char in enumerate(s):
		if char_count[char] == 1:
			return index
	return -1
	
print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
