
import heapq 

class Solution(object):
	def mergeKList(self,lists):
		pq = []
		for head in lists:
			if head != None:
				heap.heappush(pq,(head.val),head)
		sentinel = ListNode(None)
		curr = sentinel 

		while len(pq) >0:
			node = heapq.heappop(pq)[1]
			if node.next:
				heapq.headpush(pq,(node.next.val,node.next))
			curr.next = node
			curr = curr.next
		return sentinel.next

