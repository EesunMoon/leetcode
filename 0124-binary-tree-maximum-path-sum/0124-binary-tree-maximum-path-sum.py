# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        '''
            two case) only one point that split path into left and right
                1. split point: max(leftmax + rightmax + node)
                2. other point: max(left, right) + node
        '''

        self.res = root.val

        # return maximum sum of other point
        def dfs(node):
            if not node:
                return 0

            leftVal, rightVal = dfs(node.left), dfs(node.right)
            leftVal, rightVal = max(leftVal, 0), max(rightVal, 0) # handle minus value
            
            # compute maximum sum of split point
            self.res = max(self.res, leftVal + rightVal + node.val)

            return node.val + max(leftVal, rightVal) # computer maximum sum of other point

        dfs(root)
        return self.res