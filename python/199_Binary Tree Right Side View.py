#199 Binary Tree Right Side View.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.dic ={}
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.rs(root,0)
        
    def rs(self,root,level):
        if root == None:
            return
        self.dic[level] = root.val
        self.rs(root.left,level+1)
        self.rs(root.right,level+1)
        return self.dic.values()