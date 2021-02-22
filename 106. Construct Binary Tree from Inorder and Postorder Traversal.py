# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        def buildMyTree(inorder_left, inorder_right, postorder_left, postorder_right):
            if inorder_left>inorder_right:
                return None
            postorder_root = postorder_right
            index_inorder_root = index_inorder[postorder[postorder_root]]
            root = TreeNode(postorder[postorder_root])
            
            len_left = index_inorder_root - inorder_left
            
            root.left = buildMyTree(inorder_left, index_inorder_root-1, postorder_left, postorder_left+len_left-1)

            root.right = buildMyTree(index_inorder_root+1, inorder_right, postorder_left+ len_left, postorder_right-1)

            
            return root
            
        n = len(inorder)
        index_inorder = {elements: i for i, elements in enumerate(inorder)}
        return buildMyTree(0, n-1, 0, n-1)
        

if __name__ == '__main__':
    func = Solution()

    # preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    
    buildTree = func.buildTree(inorder, postorder)
    print("it is done")

