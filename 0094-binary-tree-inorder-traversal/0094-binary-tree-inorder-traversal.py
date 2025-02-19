# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []
        
        res = []
        """
            inorder: left - root - right
                using prev pointer
                1. start from root, move pointer until curr.left is none
                    every iteration, save current ptr in previous and then move ptr to left
                    if curr.left is none: append curr -> move right -> move left

        """


        ### DFS O(N) O(H) - stack
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

        ## DFS O(N) O(H) - recursion
        """
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res
        """