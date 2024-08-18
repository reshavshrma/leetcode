''' An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.
Given an integer n, return true if n is strictly palindromic and false otherwise.
A string is palindromic if it reads the same forward and backward. '''

def isStrictlyPalindromic(n):
        return False
        
print(isStrictlyPalindromic(9))
print(isStrictlyPalindromic(4))
print(isStrictlyPalindromic(3))
print(isStrictlyPalindromic(2))
print(isStrictlyPalindromic(1))
print(isStrictlyPalindromic(5))
print(isStrictlyPalindromic(6))
print(isStrictlyPalindromic(7))
print(isStrictlyPalindromic(8))
