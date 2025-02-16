# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
                3
            5       1
         6   2     0   8
            7  4
        => if p is in left subtree and q is in right subtree, the split point node is LCA
        """
        # TC O(N) SC O(N)
        parent_map = {}
        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                parent_map[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_map[node.right] = node
                stack.append(node.right)
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent_map.get(p)
        while q:
            if q in ancestors:
                return q
            q = parent_map.get(q)
        return None

        """
        # recursion TC O(N) SC O(N)
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right
        """