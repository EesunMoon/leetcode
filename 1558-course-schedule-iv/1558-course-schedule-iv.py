class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # courses node: 0~numCourses-1
        # prerequisites: [pre, nxt]
        # queries: [pre -> nxt?]
        adj = defaultdict(set)
        for prev, nxt in prerequisites:
            adj[prev].add(nxt)
        
        def bfs(u, v):
            if not u in adj:
                return False
            if v in adj[u]:
                return True
                
            q = deque([u])
            visited = set()
            visited.add(u)
            while q:
                curr = q.popleft()
                if v in adj[curr]:
                    return True
                for nxt in adj[curr]:
                    if nxt not in visited:
                        q.append(nxt)
                        visited.add(nxt)
            return False
        res = []
        for u, v in queries:
            res.append(bfs(u,v))
        return res

            