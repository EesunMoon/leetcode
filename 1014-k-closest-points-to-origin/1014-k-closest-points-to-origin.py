class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def calDist(a, b):
            return (a-0)**2 + (b-0)**2
        
        result = [] # store [x, y]
        max_heap = [] # (dist, idx)
        
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = -calDist(x, y)
            heapq.heappush(max_heap, (dist, i))
            result.append([x, y])
            if len(max_heap) > k:
                val, idx = heapq.heappop(max_heap)
                result.remove([points[idx][0], points[idx][1]])
            
        return result