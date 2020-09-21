# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def checktwotree(root1, root2):
            if (root1==None) & (root2==None):
                return True  
            if root1 and root2 and (root1.val==root2.val):
                return checktwotree(root1.right, root2.left) & checktwotree(root1.left, root2.right)
            return False
        return checktwotree(root.left, root.right)    


    
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root: return True
#         def checktwotree(left, right):
#             if (left==None) and (right==None):
#                 return True
#             elif (left==None) or (right==None):
#                 return False
#             elif (left.val!=right.val):
#                 return False
#             return checktwotree(root.right, root.left) & checktwotree(root.left, root.right)
#         return checktwotree(root.left, root.right)    
    

if __name__ == '__main__':
    p = TreeNode(1)
    p1 = TreeNode(2)
    p2 = TreeNode(2)
    p3 = TreeNode(None)
    p4 = TreeNode(3)
    p5 = TreeNode(None)
    p6 = TreeNode(4)
    p.left = p1
    p.right = p2
    p1.left = p3
    p1.right = p4
    p2.left = p5
    p2.right = p6

    func = Solution()
    output = func.isSymmetric(p)
    print(output)
