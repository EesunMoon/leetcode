# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.diameter = 0

        def getHeight(node):
            if not node:
                return 0
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            
            self.diameter = max(self.diameter, leftHeight + rightHeight)

            return 1+ max(leftHeight, rightHeight)
        getHeight(root)
        return self.diameter