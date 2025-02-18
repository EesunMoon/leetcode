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