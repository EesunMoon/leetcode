class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # initialization
        adj = defaultdict(list)
        indegree = {i: 0 for i in range(numCourses)}
        for nxt, prv in prerequisites:
            adj[prv].append(nxt)
            indegree[nxt] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # bfs
        res = []
        visited = set()
        while queue:
            for _ in range(len(queue)):
                course = queue.popleft()
                visited.add(course)
                res.append(course)
                for nxt in adj[course]:
                    indegree[nxt] -= 1
                    if nxt not in visited and indegree[nxt] == 0:
                        queue.append(nxt)

        return res if len(res) == numCourses else []
        
        