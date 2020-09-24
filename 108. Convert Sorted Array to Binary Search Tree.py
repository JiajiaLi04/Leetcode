# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def buildtree(left, right):
            
            if left>right:
                return None

            middle = (left + right)//2
            
            root = TreeNode(nums[middle])
            root.left = buildtree(left, middle-1)
            root.right = buildtree(middle+1, right)
            return root
        
        return buildtree(0, len(nums)-1)


if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    func = Solution()
    output = func.sortedArrayToBST(nums)
    print(output)


