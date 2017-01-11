#109_Convert Sorted List to Binary Search Tree.py

#如果是奇数的话，那么重点就是len div 2 
#如果是偶数个的话，那么要做出选择：要么选最左边的那个，要么选最右边的那个
#试一试分别构造出两种，然后就发现时镜面对称的，所以两个的平衡性应该是相同的. 

#首先写出dfs的方程
#观察一下，sorted list发现可以是按in order traversal的方法构造整个树

#n is lenght of linkedlist
dfs(n,linkedlist):
	if n == 0:
		return None:
	ltree = build(n,linkedlist)
	val = n.popnext()
	rtree = build(n,linkedlist)	
	return [lt, val, rt]




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        n = self.length(head)
        self.linklist = head  #python不需要申明
        return self.dfs(n)
        
    def length(self, head): # pass by referenced 
        length = 0
        while head != None:
            head = head.next
            length += 1
            
        return length
        
    def dfs(self,length):
        if length == 0:
            return 
        lefttree = self.dfs(int(length/2))
        val = self.linklist.val
        self.linklist = self.linklist.next
        root = TreeNode(val)
        righttree = self.dfs(length - int(length/2) -1)
        root.left = lefttree
        root.right = righttree
        return root
        
     
        