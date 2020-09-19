# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
方法二：辅助栈法
解题思路：
链表特点： 只能从前至后访问每个节点。
题目要求： 倒序输出节点值。
这种 先入后出 的需求可以借助 栈 来实现。
'''
# class Solution:
#     def reversePrint(self, head):
#         stack = []
#         while head:
#             stack.append(head.val)
#             head = head.next
#         return stack[::-1]

'''
方法一：递归法
利用递归： 先走至链表末端，回溯时依次将节点值加入列表 ，这样就可以实现链表值的倒序输出。
'''

class Solution:
    def reversePrint(self, head):
        if head:
            output = self.reversePrint(head.next) + [head.val] ## list 可以直接相加。[1]+[2]=[1,2]
            return output
        else:
            return []
        # return self.reversePrint(head.next) + [head.val] if head else []


if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(3)
	head.next.next = ListNode(2)
	func = Solution()
	output = func.reversePrint(head)
	print(output)
