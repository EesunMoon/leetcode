# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            Using BFS to track node as widely as possible
                - Queue: TC O(n) SC O(w = n/2) -> O(n)
            Using DFS through recursively
                - recursive stack TC O(n) SC O(H = logn when balanced) -> O(logn)
        """
        # base case
        if not root:
            return []
        res = [] # append level

        # DFS TC O(n) SC O(H = logn when balanced) = O(N)
        def dfs(node, level):
            if len(res) == level:
                res.append([]) # append level
            res[level].append(node.val)
            for next_node in [node.left, node.right]:
                if next_node:
                    dfs(next_node, level+1)
        dfs(root, 0)
        return res

        # BFS TC O(n) SC O(W = n/2) = O(n)
        Q = deque([root])
        while Q:
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