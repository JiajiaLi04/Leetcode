# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
                    
# class Solution:
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         def helper(node, lower = float('-inf'), upper = float('inf')):
#             if not node:
#                 return True
            
#             val = node.val
#             if val <= lower or val >= upper:
#                 return False
            
#             # 调用右子树时，我们需要把下界 lower 改为 root.val
#             if not helper(node.right, val, upper):
#                 return False
            
#             # 递归调用左子树时，我们需要把上界 upper 改为 root.val
#             if not helper(node.left, lower, val):
#                 return False
#             return True

#         return helper(root)

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

    

if __name__ == '__main__':
    p = TreeNode(4)
    p1 = TreeNode(2)
    p2 = TreeNode(5)
    p3 = TreeNode(1)
    p4 = TreeNode(3)
    p5 = TreeNode(None)
    p6 = TreeNode(6)
    p.left = p1
    p.right = p2
    p1.left = p3
    p1.right = p4
    p2.left = p5
    p2.right = p6

    func = Solution()
    output = func.isValidBST(p)
    print(output)