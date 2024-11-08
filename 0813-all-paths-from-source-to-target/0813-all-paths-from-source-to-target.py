class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        path = []
        if not graph or len(graph) == 0:
            return path

        n = len(graph)
        queue = deque()
        queue.append([0])
        dest = n-1
        
        while queue:
            curr_path = queue.popleft()
            curr_node = curr_path[-1]
            for next_node in graph[curr_node]:
                temp_path = curr_path[:]
                temp_path.append(next_node)
                if next_node == dest:
                    path.append(temp_path)
                else:
                    queue.append(temp_path)
        return path
        