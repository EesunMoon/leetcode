class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = {}
        graph = collections.defaultdict(list)

        # pre, nxt
        for nxt, pre in prerequisites:
            indegree[nxt] = indegree.get(nxt, 0) + 1
            graph[pre].append(nxt)
        
        node = [x for x in range(numCourses) if x not in indegree]
        
        ans = []
        while node:
            pre = node.pop()
            ans.append(pre)
            for nxt in graph[pre]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    node.append(nxt)

        return ans if len(ans) == numCourses else []
        