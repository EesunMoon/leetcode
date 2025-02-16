# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # cousin: same depth and different parent
        # only valid: left children AND right children
        # invalid:
        #   1. left children
        if not root:
            return False

        # bfs
        # queue (node, 0, prev)
        res = []
        Q = deque([(root, 0, None)])
        while Q:
            if len(res) == 2:
                break
            curr, level, prev = Q.popleft()
            if curr.val == x or curr.val == y:
                res.append([level, prev])
            if curr.left:
                Q.append([curr.left, level+1, curr])
            if curr.right:
                Q.append([curr.right, level+1, curr])
        
        nodeX, nodeY = res
        return (nodeX[0] == nodeY[0]) and (nodeX[1].val != nodeY[1].val)