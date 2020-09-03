# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##深度优先搜索(Depth-First-Search); recursive 
# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q: # special case
#             return True
#         elif not p or not q: # special case
#             return False
#         elif p.val != q.val:
#             return False
#         else:
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # recursive

# import collections
from collections import deque
## 广度优先搜索算法（Breadth-First-Search）;queue 
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        # queue1 = collections.deque([p])
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val: ## compare the value of two nodes
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2): ## decide whether these two nodes are both exits. XOR operation: return true if both are the same.
                return False
            if (not right1) ^ (not right2): ## decide whether these two nodes are both exits. XOR operation.
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2


if __name__ == '__main__':
    p = TreeNode(1)
    p1 = TreeNode(2)
    p2 = TreeNode(3)
    p3 = TreeNode(2)
    p4 = TreeNode(3)
    p.left = p1
    p.right = p2
    p1.left = p3
    p1.right = p4


    q = TreeNode(1)
    q1 = TreeNode(2)
    q2 = TreeNode(3)
    q3 = TreeNode(2)
    q4 = TreeNode(3)
    q.left = q1
    q.right = q2
    q1.left = q3
    q1.right = q4
    
    func = Solution()
    print(func.isSameTree(p, q))
