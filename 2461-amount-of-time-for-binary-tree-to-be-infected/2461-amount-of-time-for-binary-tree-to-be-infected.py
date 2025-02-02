# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
       
        # define adjacent list
        graph = defaultdict(list)
        
        def makeGraph(node, prev):
            if not node:
                return
            
            if prev:
                graph[node.val].append(prev.val)
            if node.left:
                graph[node.val].append(node.left.val)
            if node.right:
                graph[node.val].append(node.right.val)
            
            makeGraph(node.left, node)
            makeGraph(node.right, node)
        
        makeGraph(root, None)

        if not graph:
            return 0

        # BFS
        res = 0
        q = deque([start])
        seen = set()
        seen.add(start)

        while q and len(seen) < len(graph):
            for _ in range(len(q)):
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei) # infected
                        q.append(nei)
            res += 1
        return res