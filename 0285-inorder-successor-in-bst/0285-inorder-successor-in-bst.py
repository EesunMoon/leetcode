# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        
        successor = None
        
        while root:
            if p.val >= root.val:
                root=root.right
            else:
                successor = root
                root = root.left
            
        return successor      