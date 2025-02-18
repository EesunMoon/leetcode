# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        value: unique
        tree can not be empty:: #.of tree > 2
        guarantee: p, q are in the tree

        at the high level:
            1. track all node and store parent information in parent map
                parent_map[parent] = children node
            2. track p, store its parent information: p_ancesor
            3. track q's parent and check its parent in the p_ancesor
                since tracking q to the root, we can find the lowest common ancesor
        TC O(n) SC O(n)

                3
            5       1
         6   2     0   8
            7  4
        
        
        => if p is in left subtree and q is in right subtree, the split point node is LCA
        """

        # 1. make parent_map TC O(N) SC O(N)
        parent_map = {} # key: node, value: parent
        def makeParentMap(curr, parent):
            if curr:
                parent_map[curr] = parent
                makeParentMap(curr.left, curr)
                makeParentMap(curr.right, curr)
        makeParentMap(root, None)

        # 2. store p_ancesor TC O(H) SC O(H)
        p_ancesor = set()
        curr = p
        while curr:
            p_ancesor.add(curr)
            curr = parent_map[curr]
        

        # 3. track q to identify LCS
        curr = q
        while curr:
            if curr in p_ancesor:
                return curr
            curr = parent_map[curr]
        return None





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