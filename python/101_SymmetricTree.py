
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == []:
            return True
        if not root:
            return True
        return self.isMirror(root.left ,root.right)

    def isMirror(self ,leftTree ,rightTree):
        if leftTree == None and rightTree == None:
            return True

        if leftTree != None and rightTree != None:
            if leftTree.val != rightTree.val:
                return False
        else:
            return False

        return self.isMirror(leftTree.left, rightTree.right) and self.isMirror(leftTree.right, rightTree.left)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == []:
            return True
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, leftTree, rightTree):
        if leftTree == None and rightTree == None:
            return True

        if (not leftTree and rightTree) or (leftTree and not rightTree) or (leftTree.val != rightTree.val):
            return False
        return self.isMirror(leftTree.left, rightTree.right) and self.isMirror(leftTree.right, rightTree.left)


