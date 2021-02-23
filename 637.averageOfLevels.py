# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode):
        def dfs(root: TreeNode, level: int):
            if not root:
                return
            if level < len(totals):
                totals[level] += root.val
                counts[level] += 1
            else:
                totals.append(root.val)
                counts.append(1)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        counts = list()
        totals = list()
        dfs(root, 0)
        return [total / count for total, count in zip(totals, counts)]


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
    print(func.averageOfLevels(p))
