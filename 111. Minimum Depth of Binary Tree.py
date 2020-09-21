# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if root==None:
#             return 0

#         def node_depth(root1):
#             if root1==None:
#                 return  0
#             if root1:
#                 if (root1.left!=None or root1.right!=None):
#                     return 2
#                 else:
#                     return 1
#             return  min(node_depth(root1.left), node_depth(root1.right))
                   
#         return node_depth(root) + 1

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        min_depth = 10**9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        
        return min_depth + 1

        

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
    output = func.minDepth(p)
    print(output)
