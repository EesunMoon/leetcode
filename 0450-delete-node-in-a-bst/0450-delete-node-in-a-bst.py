# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        edge case)
            1. No key found
            2. not root
        
        delete: 
            not children: just delete
            only one children: delete and connect
            all children exist:
                right subtree successor(the smallest value)
        """
        if not root:
            return None
        
        # find key
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # delete node

            # 1) not children
            if not root.left and not root.right:
                return None
            # 2) only one children
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # 3) all exist
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node