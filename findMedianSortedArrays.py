''' Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. '''

def findMedianSortedArrays(nums1, nums2):
	nums3 = nums1 + nums2
	nums3.sort()

	length = len(nums3)
	
	if length % 2 != 0:
        	i = length // 2
        	return nums3[i]
	else:
        	i = length // 2
        	median = (nums3[i] + nums3[i - 1]) / 2.0
        	return round(median, 5)

nums1 = [1, 3, 2]
nums2 = [5, 4]
median = findMedianSortedArrays(nums1, nums2)
print(median) 
