# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []
        
        res = []
        
        # define leaf or not
        def isLeaf(node):
            return (not node.left) and (not node.right)
        
        # track left boundary except for leaf
        def leftBound(node):
            while node and not isLeaf(node):
                res.append(node.val)
                node = node.left if node.left else node.right
        
        def addLeaf(node):
            # DFS
            if not node:
                return 
            
            if isLeaf(node):
                res.append(node.val)
                return
            addLeaf(node.left)
            addLeaf(node.right)
        
        # track right boundary -> store in reverse order using stack
        def rightBound(node):
            # reverse
            stack = []
            while node and not isLeaf(node):
                stack.append(node.val)
                node = node.right if node.right else node.left
            while stack:
                res.append(stack.pop())
        
        # 1) add root
        if not isLeaf(root):
            res.append(root.val)
        # 2) left boundary
        leftBound(root.left)
        # 3) leaf
        addLeaf(root)
        # 4) right boundary
        rightBound(root.right)
        
            
        return res