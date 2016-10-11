class Solution(object):
    def intersect(self, nums1, nums2):
    	result = []
		for j in nums2:
			if(j in nums1):
				result.append(j)
		return result		