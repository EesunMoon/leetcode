# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # base case
        if not root:
            return False
        
        # cousins: same level, different parent
        x_info = [-1, -1] # (level, parent value)
        y_info = [-2, -2]

        Q = deque([(root, 0, None)]) # (node, level, parent)
        while Q:
            node, level, parent = Q.popleft()
            if node.val == x:
                x_info = [level, parent]
            if node.val == y:
                y_info = [level, parent]
            
            if node.left:
                Q.append([node.left, level+1, node])
            if node.right:
                Q.append([node.right, level+1, node])
        
        if x_info[0] == y_info[0] and x_info[1] != y_info[1]:
            return True
        return False


        
        
        
        
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