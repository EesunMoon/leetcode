# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        head = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                head.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        if not head:
            return False

        def dfs(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and dfs(a.left, b.left) and dfs(a.right, b.right)
        
        for cand in head:
            if dfs(cand, subRoot):
                return True
        return False