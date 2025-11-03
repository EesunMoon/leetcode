# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
        abs(height(leftSubTree) - height(rightSubTree)) <=1
        """
        if not root:
            return True
        
        def dfs(node): # return height
            if not node:
                return 0
            
            lHeight = dfs(node.left)
            if lHeight == -1:
                return -1
            rHeight = dfs(node.right)
            if rHeight == -1:
                return -1
            if abs(lHeight-rHeight) > 1:
                return -1
            return 1 + max(lHeight, rHeight)
        return dfs(root) != -1