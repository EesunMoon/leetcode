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
        q = deque([root])
        res = []
        while q:
            qLen = len(q)
            res.append(q[0].val)
            for _ in range(qLen):
                curr = q.popleft()
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        return res