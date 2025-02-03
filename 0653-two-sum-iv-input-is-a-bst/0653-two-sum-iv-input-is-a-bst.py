# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        element = []

        # inorder
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            element.append(node.val)
            inorder(node.right)
        
        inorder(root)
        print(element)
        l, r = 0, len(element)-1
        while l<r:
            cand = element[l] + element[r]
            if cand == k:
                return True
            elif cand > k:
                r -= 1
            else:
                l += 1
        return False
