'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both 
lower and upper cases, more than once.
'''

def reverseVowels(s):
	vowels = set('AEIOUaeiou')
	s = list(s)
	i, j = 0, len(s) - 1  # Two pointers, one at the start, one at the end

	while i < j:

            # Move i forward if s[i] is not a vowel
		if s[i] not in vowels:
			i += 1

            # Move j backward if s[j] is not a vowel
		elif s[j] not in vowels:
			j -= 1

 		else:
                # Swap the vowels at i and j
			s[i], s[j] = s[j], s[i]
			i += 1
			j -= 1

	return ''.join(s)
	
print(reverseVowels("IceCream"))
