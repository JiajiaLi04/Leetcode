# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

# class Solution(object):
    
#     ## Iterative method
# 	def reverseList(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: ListNode
# 		"""
# 		# 申请两个节点，pre和 cur，pre指向None
# 		pre = None
# 		cur = head
  
# 		# 遍历链表
# 		while cur:
# 			# 记录当前节点的下一个节点
# 			tmp = cur.next
# 			# 然后将当前节点指向pre
# 			cur.next = pre
# 			# pre和cur节点都前进一位
# 			pre = cur
# 			cur = tmp
# 		return pre


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ## 递归 Recursive method
        if not (head and head.next):
            return head
        
        newHead = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        return newHead



if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	func = Solution()
	output = func.reverseList(head)
	print(output.val)
