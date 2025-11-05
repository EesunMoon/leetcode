# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node): # WITHOUT Split
            if not node:
                return 0
            
            leftSub = max(dfs(node.left), 0)
            rightSub = max(dfs(node.right), 0)
            
            res[0] = max(res[0], node.val + leftSub + rightSub) ## WITH Split

            return node.val + max(leftSub, rightSub)
        
        dfs(root)
        return res[0]
