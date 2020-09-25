# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        stack_list = []
        while head:
            stack_list.append(head.val)
            head = head.next
        print(stack_list) 
        def buildtree(left, right):
            
            if left>right:
                return None

            middle = (left + right)//2
            
            root = TreeNode(stack_list[middle])
            root.left = buildtree(left, middle-1)
            root.right = buildtree(middle+1, right)
            return root        
        
        return buildtree(0, len(stack_list)-1)   





if __name__ == '__main__':
	head = ListNode(-10)
	head.next = ListNode(-3)
	head.next.next = ListNode(0)
	head.next.next.next = ListNode(5)
	head.next.next.next.next = ListNode(9)
	func = Solution()
	output = func.sortedListToBST(head)
	print(output)