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
        hashmap = {}
        
        def clone(node):
            # already cloned
            if node in hashmap:
                return hashmap[node]
            
            new = Node(node.val)
            hashmap[node] = new
            
            for nei in node.neighbors:
                new.neighbors.append(clone(nei))
            
            return new
                
        return clone(node) if node else None