# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(node, level):
            if not node:
                return res
            
            if len(res) == level:
                res.append([])
            
            res[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        return res

        
        
        # edge case
        if not root:
            return []
        
        # BFS using queue
        # TC O(n) SC O(n)
        Q = deque()
        res = []
        Q.append(root)
        while Q:
            # level
            level = []
            for _ in range(len(Q)):
                node = Q.popleft()
                level.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            res.append(level)
        return res