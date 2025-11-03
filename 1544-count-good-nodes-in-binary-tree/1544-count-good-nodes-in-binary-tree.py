# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1 # root is always considered as good.
        q = deque() # [maximum value so far, node]
        q.append((root.val, root))
        while q:
            maxVal, node = q.popleft()
            if node.left:
                if node.left.val >= maxVal:
                    res += 1
                q.append([max(node.left.val, maxVal), node.left])
            if node.right:
                if node.right.val >= maxVal:
                    res += 1
                q.append([max(node.right.val, maxVal), node.right])
        return res

