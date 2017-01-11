# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #if nums == None:
        # [] == None is false
        # not [] is true
         if not nums:
            return None
            
        
        mid = len(nums) // 2 
        
            
        t = TreeNode(nums[mid])
        t.left = self.sortedArrayToBST(nums[:mid])
        t.right = self.sortedArrayToBST(nums[mid+1:])
        return t