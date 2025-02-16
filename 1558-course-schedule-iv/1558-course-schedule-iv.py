class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # prerequisite (a, b) a -> b
        # query (a, b) a -> b

        # make adjacent graph TC O(N) SC O(N)
        indegree = {} # course: indegree
        adj = defaultdict(list)
        for pre, nxt in prerequisites:
            adj[pre].append(nxt)
            indegree[nxt] = 1 + indegree.get(nxt,0)
        
        premap = defaultdict(set) # nxt: (pre)
        Q = deque([crs for crs in range(numCourses) if crs not in indegree])
        while Q:
            crs = Q.popleft()
            for nxt in adj[crs]:
                premap[nxt].add(crs)
                for pre in premap[crs]:
                    premap[nxt].add(pre)
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    Q.append(nxt)

        # mapping through premap TC O(Q) Q:len(queries)
        res = []
        for pre, nxt in queries:
            if pre in premap[nxt]:
                res.append(True)
            else:
                res.append(False)
        return res
