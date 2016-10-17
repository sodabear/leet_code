# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
# Therefore, the question is: when are two trees a mirror reflection of each other?
# Two trees are a mirror reflection of each other if:
# Their two roots have the same value.
# The right subtree of each tree is a mirror reflection of the left subtree of the other tree.
# step 1 :定义问题:
# 要同时满足下面两个定义：
# 树的对称是：根相等，然后左子树r1和右子树r2对称
# 左右子树的对称： r1.right.val = r2.left.val and r1.right.val = r2.left.val
#  
# step 0 : 看例子
# eg: [1,2,2,3,4,4,3] is symmetric.
# eg: [1,2,2,null,3,null,3] is symmetric.
# from the example of tree, we can tell all inputs are complete binary trees.
# so we only need to compare the value rather than the shape
#
# step 2: 
#  
class Solution(object):
    def mirror(self,r1,r2):
    # root have to equal 
        if r1 == None and r2 == None:
            return True
        if r1 == None or r2 == None:
            return False
        return (r1.val == r2.val) & self.mirror(r1.right,r2.left) & self.mirror(r1.left,r2.right) 
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.mirror(root.right, root.left)
        

        