class Solution(object):
    def kClosest(self, points, k):
        dist = []
        def euclidean(x, y):
            return x**2 + y**2

        for x, y in points:
            heapq.heappush(dist, [-euclidean(x, y), [x, y]])

            if len(dist) > k:
                heapq.heappop(dist)
        
        ans = []
        while dist:
            d, point = heapq.heappop(dist)
            ans.append(point)
        
        return ans