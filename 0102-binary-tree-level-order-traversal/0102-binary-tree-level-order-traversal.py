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
        levels = []
        if not root:
            return levels
        
        def bfs(node, level):
            if len(levels) == level:
                levels.append([])
                
            levels[level].append(node.val)
            if node.left:
                bfs(node.left, level+1)
            if node.right:
                bfs(node.right, level+1)
            
        bfs(root, 0)
        return levels

        while queue:
            ele = deque