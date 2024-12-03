class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n

    def find(self, A):
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root
    
    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)

        if root_A == root_B:
            return False
        
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        
        return True

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # adj
        adj = [[] for _ in range(n)]
        for u, v in edges: # O(E)
            adj[u].append(v)
            adj[v].append(u)
        
        # check circle
        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for nei in adj[curr]:
                # backtrack
                if nei == prev:
                    continue
                # if cicle => return False immeditedly
                if not dfs(nei, curr):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n