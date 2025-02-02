# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
            leftSubtree Max + rightSubtree Max + Root
        """
        res = [root.val]
        # caculate maximum with subTree
        def dfs(node):
            if not node:
                return 0
            
            leftMax, rightMax = dfs(node.left), dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], node.val + leftMax + rightMax) # store with Split point

            return node.val + max(leftMax, rightMax) # return maximum subTree

        dfs(root)
        return res[0]