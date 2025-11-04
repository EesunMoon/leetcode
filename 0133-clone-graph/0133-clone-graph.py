"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {} # old: new
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copiedNode = Node(node.val)
            oldToNew[node] = copiedNode
            for nei in node.neighbors:
                copiedNode.neighbors.append(dfs(nei))
            return copiedNode
        return dfs(node)
            
            
        """        
        q = deque([node])

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[curr].neighbors.append(oldToNew[nei])
        """
        return oldToNew[node]