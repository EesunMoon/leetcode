class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def calDist(a, b):
            return (a-0)**2 + (b-0)**2
        
        # first k elements
        heap = [(-calDist(points[i][0], points[i][1]), i) for i in range(k)]
        heapq.heapify(heap)

        for i in range(k, len(points)):
            dist = -calDist(points[i][0], points[i][1])
            
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i)) # delete & add
                
            
        return [points[i] for (_, i) in heap]