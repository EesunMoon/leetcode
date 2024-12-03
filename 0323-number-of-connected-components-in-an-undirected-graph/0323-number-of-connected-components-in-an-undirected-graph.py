class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(curr):
            if curr in visited:
                return

            visited.add(curr)
            for nei in adj[curr]:
                dfs(nei)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
                
        return res
        