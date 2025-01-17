# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        levels = []
        def dfs(node, level):
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            if node.left:
                dfs(node.left, 1+level)
            if node.right:
                dfs(node.right, 1+level)
        
        dfs(root, 0)
        return levels