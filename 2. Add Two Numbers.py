# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # ## use the principle of addition
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     carry = 0
    #     dummpy = output = ListNode(None)
    #     while l1 or l2  or carry:
    #         carry = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
    #         output.next = ListNode(carry%10)
    #         output = output.next
    #         carry  = carry//10
    #         l1 = l1.next if l1 else None
    #         l2 = l2.next if l2 else None
    #     return dummpy.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ## 使用递归recursive
        def dfs(l, r, i):
            if not l and not r and not i: return None
            s = (l.val if l else 0) + (r.val if r else 0) + i
            node = ListNode(s % 10)
            node.next = dfs(l.next if l else None, r.next if r else None, s // 10)
            return node
        return dfs(l1, l2, 0)


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
