# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :type target: int
        :rtype: bool
        """
        def inorder(root, values):
            if not root:
                return
            inorder(root.left, values)
            values.append(root.val)
            inorder(root.right, values)

        values1, values2 = [], []
        inorder(root1, values1)
        inorder(root2, values2)

        v = set(values2)
        for num in values1:
            if target - num in v:
                return True
        return False
        