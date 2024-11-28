class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # hashmap
        preMap = {crs: [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # check if visited
        visited = set()
        def dfs(crs):
            # already visited
            if crs in visited:
                return False
            # no prerequisites
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            
            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True