class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = {}

        # caculate indegree O(V)
        for nxt, prev in prerequisites:
            graph[prev].append(nxt)
            indegree[nxt] = 1 + indegree.get(nxt, 0)
        
        # select indegree == 0 O(E)
        queue = deque()
        for e in range(numCourses):
            if e not in indegree:
                queue.append(e)

        # BFS O(E+V)
        res = []
        while queue:
            for _ in range(len(queue)):
                crs = queue.popleft() # already indegree 0
                res.append(crs)

                for nei in graph[crs]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
        return res if len(res) == numCourses else []
