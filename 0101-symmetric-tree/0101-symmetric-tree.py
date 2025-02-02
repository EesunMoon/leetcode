# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(leftSub, rightSub):
            if not leftSub and not rightSub:
                return True
            elif ((not leftSub and rightSub) or (not rightSub and leftSub) 
                    or (rightSub.val != leftSub.val)):
                return False
            
            return dfs(leftSub.right, rightSub.left) and dfs(leftSub.left, rightSub.right)

        return dfs(root.left, root.right)
