# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# define: as a binary tree in which the depth of the !two subtrees! of  !every node! never differ by more than 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        #为什么要call isBalanced on left和right ？ 
        return abs( self.height(root.left) - self.height(root.right) )	<= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) 
        
    def height(self,root):
        if root == None:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))     