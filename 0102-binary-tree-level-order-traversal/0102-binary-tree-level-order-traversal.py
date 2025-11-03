# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        def dfs(level, node):
            if not node:
                return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            dfs(level+1, node.left)
            dfs(level+1, node.right)
        
        dfs(0, root)
        return res
            