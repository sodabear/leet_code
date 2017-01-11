310_Minimum Height Trees.py

run time is N^3
dfs(s)
  self.visited[s] = true
  for child in childrens:
    if not visited():
        dfs(child)
        visited = [true]

children(s):
    ans = []
    for v, u in edges:
        if v == s:
        ans.append(u)
        if u  == s:
        ans.append(v)



run time is fast
 

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.e = edges
        res = {}
        for i in range(n):
            res[self.dfs(i)] = i
        k = res.keys()
        k = sorted(k)
        min = min(k)
        ans = []
        for x in k:
            if x == min:
                ans.append(res[x])
        return ans    
            
    def dfs(self,r):
        if not r:
            return -1
        self.visited = {}
        self.visited[r] = True
        children = []
        for v, u in self.e:
            if v == r:
                children.append(u)
            if u == r:
                children.append(v)
        k = [0] # what if you dont have child? and using k =[]?  max(k)        
        for c in children:
            if c not in self.visited:
                self.visited[c] = True
                k.append(1+self.dfs(c))
            
        return max(k)        
            
 class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.e = edges
        res = {}
        for i in range(n):
            self.visited = {}
            res[i] = self.dfs(i)
        v = res.values()
        value = sorted(v)
        min1 = min(value)
        ans = []
        for i in range(n):
            if res[i] == min1:
                ans.append(i)
        return ans
        
            
    def dfs(self,r):
        self.visited[r] = True
        children = []
        for v, u in self.e:
            if v == r:
                children.append(u)
            if u == r:
                children.append(v)
        k = [0] # what if you dont have child? and using k =[]?  max(k)        
        for c in children:
            if c not in self.visited:
                k.append(1+self.dfs(c))
            
        return max(k)        
                
                
      树的重心，
      

      def findMinHeightTrees(self, n, edges):
    if n == 1: return [0] 
    adj = [set() for _ in xrange(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)

    leaves = [i for i in xrange(n) if len(adj[i]) == 1]

    while n > 2:
        n -= len(leaves)
        newLeaves = []
        for i in leaves:
            j = adj[i].pop()
            adj[j].remove(i)
            if len(adj[j]) == 1: newLeaves.append(j)
        leaves = newLeaves
    return leaves
    
# Runtime : 104ms

hight of tree starts from 0 
找到所有leave 然后砍掉砍掉砍掉
剥洋葱                             
The actual implementation is similar to the BFS topological sort. Remove the leaves, update the degrees of inner vertexes. Then remove the new leaves. Doing so level by level until there are 2 or 1 nodes left. What's left is our answer!


Why there are at most 2 MHT? Thank you!
Imagine you remove the leaves level by level. If there are more than 3 nodes left it can not be all leaves. You can find that out by definition of leaves and tree.