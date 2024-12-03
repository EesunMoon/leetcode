class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        hashset = [[] for _ in range(numCourses)]
        indegree = {}
        for nxt, prv in prerequisites:
            hashset[prv].append(nxt)
            indegree[nxt] = 1 + indegree.get(nxt, 0)
        
        queue = deque(i for i in range(numCourses) if i not in indegree)
        if not queue:
            return False
        seen = set()
        while queue:
            crs = queue.popleft()
            seen.add(crs)
            for nxt in hashset[crs]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return len(seen) == numCourses
