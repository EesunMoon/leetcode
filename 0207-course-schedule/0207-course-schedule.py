class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = {}
        for nxt, prv in prerequisites:
            graph[prv].append(nxt)
            indegree[nxt] = 1 + indegree.get(nxt, 0)
        
        queue = deque([crs for crs in range(numCourses) if crs not in indegree])
        seen = set()
        while queue:
            for _ in range(len(queue)):
                crs = queue.popleft()
                seen.add(crs)
                for nei in graph[crs]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
        
        return len(seen) == numCourses