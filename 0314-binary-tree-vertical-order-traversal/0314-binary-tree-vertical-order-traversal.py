# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
                3
             9.    20
        4.     01.     7
        """
        if not root:
            return []

        hashmap = defaultdict(list) # index: []
        max_index = float("-INF")
        min_index = float("INF")
        Q = deque([(root, 0)]) # (node, index)
        while Q:
            node, idx = Q.popleft()
            hashmap[idx].append(node.val)

            max_index = max(max_index, idx)
            min_index = min(min_index, idx)
            if node.left:
                Q.append([node.left, idx-1])
            if node.right:
                Q.append([node.right, idx+1])

        # TC O(W)
        res = []
        for idx in range(min_index, max_index+1):
            if idx in hashmap:
                res.append(hashmap[idx])
        return res
