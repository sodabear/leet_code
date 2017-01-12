class Solution(object):
    def generate(self, i, j):
        l = []
        if i > j: l.append(None)
        for k in xrange(i, j+1):
            left = self.generate(i, k-1)
            right = self.generate(k+1, j)
            for nodeleft in left:
                for noderight in right:
                    root = TreeNode(k)
                    root.left = nodeleft
                    root.right = noderight
                    l.append(root)
        return l
    
    def generateTrees(self, n):
        if n == 0: return []
        return self.generate(1, n)