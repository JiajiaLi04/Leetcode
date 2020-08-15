# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        dummyHead = ListNode(0)
        
        dummyHead.next = head
        while head != None and head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummyHead.next

