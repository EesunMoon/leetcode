class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        adj = [[] for i in range(len(edges)+1)]
        # visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                
                if not dfs(nei, curr):
                    return False
            
            return True
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()

            if not dfs(u, -1):
                return [u, v]