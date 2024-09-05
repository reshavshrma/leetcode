'''
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

    answer1 : the number of indices i such that nums1[i] exists in nums2.
    answer2 : the number of indices i such that nums2[i] exists in nums1.

Return [answer1,answer2]
'''

def findIntersectionValues(nums1, nums2):
	
	found1, found2 = 0,0
	
	#check in array 1
	for num in nums1:
		if num in nums2:
			found1 += 1
			
	#check in array 2
	for num in nums2:
		if num in nums1:
			found2 += 1
			
	return[found1, found2]
	
nums1 = [2,3,2]
nums2 = [1,2]
nums3 = [4,3,2,3,1]
nums4 = [2,2,5,2,3,6]
print(findIntersectionValues(nums1, nums2))
print(findIntersectionValues(nums3, nums4))
