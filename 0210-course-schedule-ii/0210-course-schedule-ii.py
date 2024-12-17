class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # initialize: post, pre => T O(E), S O(E+V)
        adj = defaultdict(list)
        indegree = {}

        for post, pre in prerequisites:
            adj[pre].append(post)
            indegree[post] = indegree.get(post, 0) + 1
        
        # bfs => T O(E+V), S O(E+V)
        ans = []
        queue = deque()
        for cur in range(0, numCourses):
            if cur not in indegree:
                queue.append(cur)
        
        while queue:
            crs = queue.popleft()
            ans.append(crs)
            if crs in adj:
                for nei in adj[crs]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        return ans if len(ans) == numCourses else []


        
        
        
        