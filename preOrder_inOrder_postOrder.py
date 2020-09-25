class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

## stack: 
class Solution:
    # 先序打印二叉树（递归). preOrderTraverse前序遍历:根节点->左子树->右子树
    # 1245367
    def preOrderTraverse(self, node):
        def pre(node):
            if not node:
                return None
            stack.append(node.val)
            pre(node.left)
            pre(node.right)
            return stack
        stack = []
        return pre(node)

    # 先序打印二叉树（非递归). preOrderTraverse    
    # 1245367
    def preOrderTraveseV2(self, node):
        stack = [node]
        output = []
        while len(stack) > 0:
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()
        return output
    
    ## 中序遍历: 左子树->根节点->右子树
    # 中序打印二叉树（递归）. 4251637
    def inOrderTraverse(self, node):
        def inorder(node): 
            if node is None:
                return None
            inorder(node.left)
            stack.append(node.val)
            inorder(node.right)
            return stack  
        stack = []
        return inorder(node)
    # 中序打印二叉树（非递归): 左子树->根节点->右子树.4251637
    def inOrderTraverseV2(self, node):
        stack = []
        pos = node
        output = []
        while pos or len(stack) > 0:
            ## store pos.left into stack
            if pos:
                stack.append(pos)
                pos = pos.left
            ## after all of left nodes are stored in stack, the pos becames None. Then using the property of stack: last in, first out. 
            else:
                pos = stack.pop()
                output.append(pos.val)
                ## do not forget the right node.
                pos = pos.right
        return output
    
    ## 后序遍历: 左子树->右子树->根节点
    # 后序打印二叉树（递归）4526731
    def postOrderTraverse(self, node):
        def postorder(node):
            if node is None:
                return None
            postorder(node.left)
            postorder(node.right)
            stack.append(node.val)
            return stack
        stack = []
        return postorder(node)
    

    # 后序打印二叉树（非递归）
    # 使用两个栈结构
    # 第一个栈进栈顺序：左节点->右节点->跟节点
    # 第一个栈弹出顺序： 跟节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
    # 第二个栈存储为第一个栈的每个弹出依次进栈
    # 最后第二个栈依次出栈
    def postOrderTraverseV2(self, node):
        stack = [node]
        stack2 = []
        while len(stack) > 0:
            node = stack.pop()
            stack2.append(node)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        while len(stack2) > 0:
            print(stack2.pop().val)       


if __name__ == '__main__':
    
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    
    func = Solution()
    output = func.postOrderTraverseV2(a)
    print(output)