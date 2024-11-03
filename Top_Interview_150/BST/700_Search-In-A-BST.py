# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # option1) Recursive
        if root is None or val==root.val:
            return root
        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)

        """
        # option2) Iterative
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root=root.left
            else:
                root=root.right
        """
