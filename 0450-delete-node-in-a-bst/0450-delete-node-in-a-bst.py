# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def successor(self, root):
        # successor: the next node, or the smallest node after the current one
        # go to the right once, and then as many time to the left
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        # predecessor: previous node in the inorder traversal
        # go to the left once and then as many time to the right
        root = root.left
        while root.right:
            root=root.right
        return root.val

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        # delete from right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete from current node
        else:
            # 1) node is leaf
            if not (root.left or root.right):
                root = None
            # 2) node has one right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # 3) node has one right child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        
        return root