import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def man_dist(p1, p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        
        n = len(points)
        visited = [False] * n
        dist_info = []
        edge_limited = 0 # until n-1
        total_weight = 0
        
        # Start with the first points
        for i in range(1, n):
            weight = man_dist(points[0], points[i])
            dist_info.append((weight, 0, i))
        visited[0] = True

        # sorted with ascending order
        heapq.heapify(dist_info)

        while dist_info and edge_limited < n-1:
            weight, p1, p2 = heapq.heappop(dist_info)
            if not visited[p2]:
                visited[p2] = True
                total_weight += weight
                for i in range(n):
                    if not visited[i]:
                        weight = man_dist(points[p2], points[i])
                        heapq.heappush(dist_info, (weight, p2, i))
                edge_limited += 1
        
        return total_weight