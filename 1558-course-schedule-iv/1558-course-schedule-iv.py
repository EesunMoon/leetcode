class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # courses node: 0~numCourses-1
        # prerequisites: [pre, nxt]
        # queries: [pre -> nxt?]
        adj = defaultdict(set) # SC O(V)
        indegree = [0] * numCourses # SC O(V)
        for prev, nxt in prerequisites: # TC O(P)
            adj[prev].add(nxt)
            indegree[nxt] += 1
        isPre = [set() for _ in range(numCourses)] # TC O(V) SC O(V+E) crs:set(prev)
        
        q = deque([crs for crs in range(numCourses) if indegree[crs]==0])
        while q:
            crs = q.popleft()
            for nxt in adj[crs]:
                isPre[nxt].add(crs)
                isPre[nxt].update(isPre[crs])
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return [ u in isPre[v] for u, v in queries]

            