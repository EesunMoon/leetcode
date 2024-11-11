class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        indegree = {}
        for post, pre in prerequisites:
            graph[pre].append(post)
            indegree[post] = indegree.get(post, 0)+1
        queue = deque(
            [k for k in range(numCourses) if k not in indegree]
        )

        answer = []
        while queue:
            course = queue.popleft()
            answer.append(course)

            if course not in graph:
                continue
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)


        return answer if len(answer) == numCourses else []
        