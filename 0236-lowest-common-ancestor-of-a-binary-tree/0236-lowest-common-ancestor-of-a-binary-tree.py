# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # DFS
        if (root is None) or (root is p) or (root is q):
            return root # None or p or q
        # search left or right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p or q in both side
        if left and right:
            return root
        
        # only one side
        return left if left else right

        """ BFS 
        # 1. parent map --> O(N), O(N)
        parMap = {root:None}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                parMap[node.left] = node
                stack.append(node.left)
            if node.right:
                parMap[node.right] = node
                stack.append(node.right)
            if p in parMap and q in parMap:
                break
        
        # 2. p_parent --> O(H)
        cand = set()
        while p:
            cand.add(p)
            p = parMap[p]
        
        # 3. find LCA
        while q:
            if q in cand:
                return q
            q = parMap[q]
        
        return None
        """
