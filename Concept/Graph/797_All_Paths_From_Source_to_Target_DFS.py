class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        path = []
        if not graph or len(graph) == 0:
            return path

        def dfs(node):
            curr_path.append(node)
            if node == dest:
                paths.append(curr_path[:])
                return
            
            for next_node in graph[node]:
                dfs(next_node)
                curr_path.pop()

        dest = len(graph)-1
        paths = []
        curr_path = []
        dfs(0)
        return paths
        
