# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)

            return max(left_depth, right_depth) + 1
        
if __name__ == '__main__':
    p = TreeNode(3)
    p1 = TreeNode(9)
    p2 = TreeNode(20)
    p3 = TreeNode(15)
    p4 = TreeNode(7)
    p.left = p1
    p.right = p2
    p2.left = p3
    p2.right = p4

    func = Solution()
    print(func.maxDepth(p))