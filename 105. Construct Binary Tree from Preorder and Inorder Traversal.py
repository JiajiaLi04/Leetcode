## Offer 07


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# if __name__ == '__main__':
#     func = Solution()

#     preorder = [3,9,20,15,7]
#     inorder = [9,3,15,20,7]
    
#     buildTree = func.buildTree(preorder, inorder)
#     print("it is done")
# #####----------------------------------------------

'''
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/qian-xu-bian-li-python-dai-ma-java-dai-ma-by-liwei/
'''

## recursive
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            
            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点. 
        ## a directory
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)




# from typing import List
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         pre_len = len(preorder)
#         in_len = len(inorder)
#         if pre_len != in_len:
#             raise Exception('数据输入错误')
#         root = self.__build_tree(preorder, 0, pre_len - 1, inorder, 0, in_len - 1)
#         return root

#     def __build_tree(self, preorder, pre_left, pre_right,
#                      inorder, in_left, in_right):
#         if pre_left > pre_right or in_left > in_right:
#             return None

#         pivot = preorder[pre_left]
#         pivot_index = in_left
#         while inorder[pivot_index] != pivot:
#             pivot_index += 1
#         root = TreeNode(pivot)
#         root.left = self.__build_tree(preorder, pre_left + 1, pre_left + pivot_index - in_left,
#                                       inorder, in_left, pivot_index - 1)

#         root.right = self.__build_tree(preorder, pre_left + pivot_index - in_left + 1, pre_right,
#                                        inorder, pivot_index + 1, in_right)
#         return root


if __name__ == '__main__':
    func = Solution()

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    
    buildTree = func.buildTree(preorder, inorder)
    print("it is done")

