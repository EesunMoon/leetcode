# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: curr, left, right (first value is always root)
        # inorder: left, curr, right (left index boundary, right index boundary)
        if not preorder or not inorder:
            return None
        rootVal, rootIdx = preorder[0], inorder.index(preorder[0])
        root = TreeNode(rootVal)

        root.left = self.buildTree(preorder[1:rootIdx+1], inorder[:rootIdx])
        root.right = self.buildTree(preorder[rootIdx+1:], inorder[rootIdx+1:])
        return root