# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 1) parents info: from root to the p and q -> TC O(n) SC O(n)
        parent ={root: None}
        stack = [root]
        while p not in parent or q not in parent:
            curr = stack.pop()
            if curr.left:
                parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                stack.append(curr.right)
        
        # 2) save p's ancestor set
        p_anc = set()
        while p:
            p_anc.add(p)
            p = parent[p]

        # 3) find LCA by tracking nodes from q to root
        while q:
            if q in p_anc:
                return q
            q = parent[q]

