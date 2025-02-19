# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            recursive: DFS
                if p is in the right side and q is in the left side -> LCA: root
                if p is in the right/left side and root is q OR 
                    q is in the right/left side and root is p       -> LCA: root 
        """
        # TC O(N) SC O(H)
        def dfs(node):
            # base case:
            if (not node) or (node == p) or (node == q):
                return node

            # track left subtree and right subtree
            left = dfs(node.left)
            right = dfs(node.right)

            # find p and q in the both side
            if left and right:
                return node
            
            # there should be exist in one side
            return left if left else right
        return dfs(root)
        

        """
            don't use parent map
                1. add parent information in the node instead of using parent map
                2. use pointer - as detecting circular in the linked list O(N)

        """
        ## Total TC O(N) SC O(H)
        # # 1. add parent information in the node: TC O(N) SC O(H)
        # def assignParent(curr, parent):
        #     if curr:
        #         curr.parent = parent
        #         assignParent(curr.left, curr)
        #         assignParent(curr.right, curr)
        # assignParent(root, None)

        # # 2. find LCA using parent pointer: TC O(N) SC O(1)
        # p_ptr, q_ptr = p, q
        # while p_ptr!=q_ptr:
        #     p_ptr = p_ptr.parent if p_ptr else p
        #     q_ptr = q_ptr.parent if q_ptr else q
        # return p_ptr
        
        
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
        ### Total: TC O(N) SC O(N)
        # # 1. make parent_map TC O(N) SC O(N)
        # parent_map = {} # key: node, value: parent
        # def makeParentMap(curr, parent):
        #     if curr:
        #         parent_map[curr] = parent
        #         if curr.left:
        #             makeParentMap(curr.left, curr)
        #         if curr.right:
        #             makeParentMap(curr.right, curr)
        # makeParentMap(root, None)

        # # 2. store p_ancesor TC O(H) SC O(H)
        # p_ancesor = set()
        # curr = p
        # while curr:
        #     p_ancesor.add(curr)
        #     curr = parent_map[curr]
        

        # # 3. track q to identify LCS
        # curr = q
        # while curr:
        #     if curr in p_ancesor:
        #         return curr
        #     curr = parent_map[curr]
        # return None