class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [] # heap (-dist, (x, y)) O(klogk) O(k)
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(res, (-dist, (x, y)))
            if len(res) > k:
                heapq.heappop(res)
        return [[x, y] for _, (x, y) in res]
