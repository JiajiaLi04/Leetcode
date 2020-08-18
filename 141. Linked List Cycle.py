# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
        
# ## hash map
#     def hasCycle(self, head: ListNode) -> bool:
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         lookup = set()
#         p = head
#         while p:
#             lookup.add(p)
#             if p.next in lookup:
#                 return True
#             p = p.next
#         return False


## two pointers. one is slow and another is fast
	def hasCycle(self, head):
			"""
			:type head: ListNode
			:rtype: bool
			"""
			slow = head
			fast = head
			while fast and fast.next:
				slow = slow.next
				fast = fast.next.next
				if slow == fast:
					return True
			return False




if __name__ == '__main__':
	head = ListNode(3)
	head.next = ListNode(2)
	head.next.next = ListNode(0)
	head.next.next.next = ListNode(-4)
	head.next.next.next = head.next
	func = Solution()
	output = func.hasCycle(head)
	print(output)
