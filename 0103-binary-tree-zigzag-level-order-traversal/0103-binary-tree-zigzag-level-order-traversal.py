# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # TC O(n) SC O(n)
        # base case
        if not root:
            return []
        
        # queue - level order (first in first out)
        Q = deque([root])
        res = []
        while Q:
            # for each level
            level = deque()
            for _ in range(len(Q)):
                # manipulate at append stage
                node = Q.popleft()
                if len(res) % 2 == 0: 
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                # typical level order traversal
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                
            res.append(list(level))
        return res