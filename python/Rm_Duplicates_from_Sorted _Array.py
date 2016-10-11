"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.
"""

""" 
Intuition 1: 
111234455577
122234455577
123334455577
123444455577
123455555577
123457777777

Intuition 2:
111234455577
121234455577
123234455577
1
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #print(nums)
        length = len(nums)
        # DONT FORGET BASE CASE!!!!!!!!!!!
        if length == 0:
            return 0
        searcher = 0 
        locater = 0 
        #termination case is after we search the whole array. 
        while searcher <= length - 1:
        	if nums[locater] ==  nums[searcher]:
        		searcher = searcher + 1
        		print(searcher)
        	else: 
        		nums[locater+1] = nums[searcher]
        		locater = locater + 1
        		searcher = searcher + 1
        		print(locater)

        return locater + 1		

