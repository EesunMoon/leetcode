# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ## [Optimal] BFS - TC O(n) SC O(W) W: width
        """
        queue = ([pair]) 
            << [root, root] 
            [root.left, root.right]
            [left.left, right.right], [left.right, right.left]
            ..
        """
        Q = deque([(root, root)])
        while Q:
            left, right = Q.popleft()
            
            if not left and not right: # Null - no have children
                continue
            if (not left or not right) or (left.val != right.val):
                return False
            
            Q.append([left.left, right.right])
            Q.append([left.right, right.left])
        
        return True
        
        ## DFS - TC O(n) SC O(n)
        """
            valid
                leftSubTree(o) and rightSubTree (o) && value is same
                leftSubTree(x) and rightSubTree (x)
            
                - base case) left empty and right emtpy -> True
                - Invalid case) left empty or right empty -> False
                                left.val != right.val -> False
                
                1. input: left, right
                2. recursion: (left.right, right.left) and (left.left, right.right)
                    left == right
                    left.right == right.left
                    left.left == right.right
        """
        # TC O(n) SC O(n)
        if not root:
            return True
        
        def dfs(leftSub, rightSub):
            # base case
            if not leftSub and not rightSub:
                return True
            elif (not leftSub or not rightSub) or (leftSub.val != rightSub.val):
                return False
            
            return dfs(leftSub.right, rightSub.left) and dfs(leftSub.left, rightSub.right)
        
        return dfs(root.left, root.right)
        