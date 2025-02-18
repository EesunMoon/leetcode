# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        """
            DFS TC O(n) SC O(H)
        """
        def dfs(node, level):
            if len(res) == level:
                res.append(node.val)
            """
                if we want to left side: [node.left, node.right]
                in this question we want to save right side => [node.right, node.left]
            """
            for next_node in [node.right, node.left]: # we want to see right side first
                if next_node:
                    dfs(next_node, level+1)
        dfs(root, 0)
        return res


        """
            BFS TC O(n) SC O(W = n/2)
        """
        # not using additional level array
        Q = deque([root])
        while Q:
            for _ in range(len(Q)):
                node = Q.popleft()
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            res.append(node.val)
        return res
        """
        ## Two list
        Q = deque()
        Q.append(root)
        while Q:
            level = []
            for _ in range(len(Q)):
                node = Q.popleft()
                level.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            res.append(level[-1])
        return res
        """