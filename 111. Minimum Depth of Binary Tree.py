# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 这道题递归条件里分为三种情况
        # 1.左孩子和有孩子都为空的情况，说明到达了叶子节点，直接返回1即可
        if not root.left and not root.right:
            return 1
   
        min_depth = 10**9
        #2.如果左孩子和由孩子其中一个为空，那么需要返回比较大的那个孩子的深度        
        m1 = min_depth(root.left)
        m2 = min_depth(root.right)
        # 这里其中一个节点为空，说明m1和m2有一个必然为0，所以可以返回m1 + m2 + 1;
        if root.left==None or root.right==None:
            return m1 + m2 +1
        # 3.最后一种情况，也就是左右孩子都不为空，返回最小深度+1即可
        return min_depth +1    

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
