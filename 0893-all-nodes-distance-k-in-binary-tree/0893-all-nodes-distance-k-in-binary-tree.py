# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # build adjacent graph
        graph = defaultdict(list)
        def makeGraph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            makeGraph(node.left, node)
            makeGraph(node.right, node)
        makeGraph(root, None)

        # bfs to find nodes distance k
        Q = deque([target.val])
        seen = set([target.val])
        while Q or k > 0:
            if k == 0:
                return list(Q)
            for _ in range(len(Q)):
                node = Q.popleft()
                for nei in graph[node]:
                    if nei not in seen:
                        Q.append(nei)
                        seen.add(nei)
            k -= 1
        return []