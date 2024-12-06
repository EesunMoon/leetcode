"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        graph={} # Node address: Node

        def clone(curr):
            # already in graph hashmap
            if curr in graph:
                return graph[curr]
            
            # create new node
            new = Node(curr.val)
            graph[curr] = new

            # connect neighbors to new(clone) node
            for nei in curr.neighbors:
                new.neighbors.append(clone(nei))
            
            return new

        return clone(node) if node else None
        