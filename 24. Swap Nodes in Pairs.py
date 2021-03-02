# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head=null or head.next=null:
            return head
        else:
            newNode = head.next
            head.next = self.swapPairs(newNode.next)
            newNode.next.next = head
        return newNode

        
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    func = Solution()
    print(func.swapPairs(p))
        