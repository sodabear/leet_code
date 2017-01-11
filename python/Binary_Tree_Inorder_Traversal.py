
#For instance, if the "processing" is just printing, 
#a tree is printed as "(left subtree) root (right subtree)." 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root == None:
            return []
        #为什么append的这样不行啊？
        #ans.append(self.inorderTraversal(root.left))
        #ans.append(root.val)
        #ans.append(self.inorderTraversal(root.right))
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)