"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

hint: use two pointer to keep tracking it. 
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        thrower = len(nums)-1 # thrower = len(nums)
        catcher = 0
        while catcher <= thrower: #catcher < thrower 
            if nums[catcher] == val:
                nums[catcher] = nums[thrower] #nums[catcher] = nums[thrower -1]
                thrower = thrower - 1
                
            else: 
    			catcher = catcher + 1		
    	return catcher 			

