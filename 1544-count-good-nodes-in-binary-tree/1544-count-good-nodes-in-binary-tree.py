# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 1 # contain root node

        def dfs(node, maxVal):
            if not node:
                return None
            
            maxVal = max(maxVal, node.val)
            if node.left and maxVal <= node.left.val:
                self.res += 1
            if node.right and maxVal <= node.right.val:
                self.res +=1
            
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, root.val)
        return self.res