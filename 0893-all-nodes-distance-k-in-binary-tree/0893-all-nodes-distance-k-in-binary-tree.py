# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        1. adjacent graph TC O(n) SC O(n)
        2. BFS TC O(n) SC O(n)
        """
        # 1. build adjacent graph
        adj = defaultdict(list)
        def makeGraph(node, parent):
            if parent:
                adj[node.val].append(parent.val)
            if node.left:
                adj[node.val].append(node.left.val)
                makeGraph(node.left, node)
            if node.right:
                adj[node.val].append(node.right.val)
                makeGraph(node.right, node)
        makeGraph(root, None)

        # 2. BFS- starting from target node
        Q = deque([target.val]) # append val
        seen = set()
        seen.add(target.val)
        while Q:
            if k == 0:
                return list(Q)
            for _ in range(len(Q)):
                node = Q.popleft()
                for nei in adj[node]:
                    if nei not in seen:
                        Q.append(nei)
                    seen.add(nei)
            k -= 1
        return []