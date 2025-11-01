# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ BFS TC O(n) SC O(n)
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
        """
        # DFS - recursion
        res = []

        def dfs(node, level):
            if not node:
                return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)

            # next stage
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        return res


        