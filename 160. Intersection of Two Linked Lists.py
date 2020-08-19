# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        return ListNode(1)





if __name__ == '__main__':
	headA = ListNode(1)
	headA.next = ListNode(9)
	headA.next.next = ListNode(1)
	headA.next.next.next = ListNode(2)
	headA.next.next.next.next = ListNode(4)

	headB = ListNode(3)
	headB.next = headA.next.next.next

	func = Solution()
	output = func.getIntersectionNode(headA, headB)
	print(output.val)
