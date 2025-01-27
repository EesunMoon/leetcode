# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        element = []

        # save element in array
        def inorder(node):
            # we cannot search target
            if not node:
                return

            inorder(node.left)
            element.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # two sum: using two pointer
        l, r = 0, len(element)-1
        while l<r:
            curr = element[l] + element[r]
            if curr == k:
                return True
            elif curr < k:
                l += 1
            else:
                r -= 1

        return False