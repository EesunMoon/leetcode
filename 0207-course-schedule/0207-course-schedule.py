class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## [a,b]: b-->a
        ## Node: 0~numCourses

        # 1. adj list T O(m) S O(n)
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for nxt, prv in prerequisites:
            adj[prv].append(nxt)
            indegree[nxt] += 1
        
        # 2. indegree == 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # 3. bfs
        while q:
            crs = q.popleft()
            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return sum(indegree) == 0