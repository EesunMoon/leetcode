# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1. parent map
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
        
        # 2. p_parent
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