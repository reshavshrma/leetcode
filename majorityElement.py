'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
'''

def majorityElement(nums):
	candidate = None
	count = 0
	
	for num in nums:
		if count == 0:
			candidate = num
		if num == candidate:
			count += 1
		else:
			count -= 1
	return candidate
	
print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
