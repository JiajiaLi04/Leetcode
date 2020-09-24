# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def checktree(root):
#             if not root:
#                 return True
            
#             if root.left and root.right:                    
#                 if root.left.val<root.val and root.right.val> root.val:
#                     return True
            
#             return checktree(root.left) and checktree(root.right)
#         return checktree(root)
                    
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            # 调用右子树时，我们需要把下界 lower 改为 root.val
            if not helper(node.right, val, upper):
                return False
            
            # 递归调用左子树时，我们需要把上界 upper 改为 root.val
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
         
        
        


if __name__ == '__main__':
    p = TreeNode(1)
    p1 = TreeNode(2)
    p2 = TreeNode(3)
    p3 = TreeNode(4)
    p4 = TreeNode(None)
    p5 = TreeNode(None)
    p6 = TreeNode(5)
    p.left = p1
    p.right = p2
    p1.left = p3
    p1.right = p4
    p2.left = p5
    p2.right = p6

    func = Solution()
    output = func.isValidBST(p)
    print(output)