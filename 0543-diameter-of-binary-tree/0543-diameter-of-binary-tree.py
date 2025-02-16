# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        maximum length of leftsubTree + maximum length of rightsubTree
        """
        self.res = 0
        def getLength(node):
            if not node:
                return 0
            left = getLength(node.left)
            right = getLength(node.right)

            self.res = max(left + right, self.res)

            return max(left, right) + 1
        getLength(root)
        return self.res