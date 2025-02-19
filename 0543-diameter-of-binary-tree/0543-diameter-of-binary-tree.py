# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        maximum length of leftsubTree + maximum length of rightsubTree
            DFS - return height:: max(left, right) + 1
                inside: calculate maximum diameter:: res = max(res, 1+left+right)
        """
        # TC O(N) SC O(H)
        self.res = 0
        def dfs(node): # return height of subTree
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # update diameter
            self.res = max(self.res, left + right)

            return max(left, right) + 1 # return height of subTree
        dfs(root)
        return self.res