# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        output = ListNode(None)
        while l1 and l2 :
            value = (l1.val + l2.val)%10 + carry
            carry = (l1.val + l2.val)//10
            output.next = ListNode(value)
            l1 = l1.next
            l2 = l2.next 
        return output.next

if __name__ == '__main__':
    headA = ListNode(2)
    headA.next = ListNode(4)
    headA.next.next = ListNode(3)


    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(4)

    func = Solution()
    output = func.addTwoNumbers(headA, headB)
    print(output.val)
