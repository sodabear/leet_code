"""
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

use two pointer
"""

class Solution(object):
	def moveZeroes(self,nums):
		point0 = 0
		for i in range(0,len(nums)):
			if nums[i] != 0:
				nums[point0],nums[i] = nums[i],nums[point0]
				point0 = point0 + 1	