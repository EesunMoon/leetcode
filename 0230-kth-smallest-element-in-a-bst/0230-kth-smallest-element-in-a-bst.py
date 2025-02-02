# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder => select? TC O(n) SC O(n)
        """
        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res[k-1]
        """

        # stack - dfs
        stack = []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            res = stack.pop()
            k -= 1
            if k == 0:
                return res.val
            curr = res.right
