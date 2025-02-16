# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # [-10, -3, 0, 5, 9]
        # preorder: node -> left -> right
        
        def preorder(l, r):
            if l > r:
                return None
            
            m = (l+r)//2 # parent
            
            root = TreeNode(nums[m])
            root.left = preorder(l, m-1)
            root.right = preorder(m+1, r)
            return root
        return preorder(0, len(nums)-1)
