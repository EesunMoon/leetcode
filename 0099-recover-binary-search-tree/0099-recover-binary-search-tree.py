# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
            3
        1       4
              2
        inorder =  [1, 3, 2, 4]
        """
        # using only two pointer SC O(1)
        first, second = None, None
        prev = None
        curr = root
        while curr:
            if not curr.left:
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if not temp.right:
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        # Inorder traversal SC O(n)
        """
        inorder = []
        def traversal(node):
            if not node:
                return
            
            traversal(node.left)
            inorder.append(node)
            traversal(node.right)
        traversal(root)
        
        first, second = None, None # to ensure finding last error point
        for i in range(len(inorder)-1):
            if inorder[i].val > inorder[i+1].val:
                if not first:
                    first = inorder[i]
                second = inorder[i+1]
        """
        first.val, second.val = second.val, first.val