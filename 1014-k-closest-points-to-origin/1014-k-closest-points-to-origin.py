class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [] # max heap (- dist, idx)

        for i in range(len(points)):
            dist = -(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(dists, (dist, i))
            if len(dists) > k:
                heapq.heappop(dists)
        return [points[i] for _, i in dists]
            
