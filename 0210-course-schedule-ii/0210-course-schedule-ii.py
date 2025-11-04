class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [a,b] b->a
        adj = defaultdict(list)
        indegree = [0]*numCourses
        for crs, prereq in prerequisites:
            adj[prereq].append(crs)
            indegree[crs] += 1
        
        q = deque([crs for crs in range(numCourses) if indegree[crs] == 0])

        order = []
        while q:
            crs = q.popleft()
            order.append(crs)
            for nxt in adj[crs]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return order if len(order) == numCourses else []
