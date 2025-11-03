# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
        abs(height(leftSubTree) - height(rightSubTree)) <=1
        """
        if not root:
            return True
        
        def getHeight(node):
            # return [balanced_flag, height]
            if not node:
                return [True, 0]
            
            leftFlag, leftHeight = getHeight(node.left)
            rightFlag, rightHeight = getHeight(node.right)

            flag = leftFlag and rightFlag and abs(leftHeight-rightHeight) <= 1

            return [flag, 1 + max(leftHeight, rightHeight)]
            
        return getHeight(root)[0]