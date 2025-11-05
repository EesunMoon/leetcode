class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            x1, y1 = points[p1]
            x2, y2 = points[p2]
            return abs(x1-x2)+abs(y1-y2)
        
        n = len(points)
        cost = 0
        minHeap = [(0,0)] # dist, point
        visited = set()

        # TC O(n**2*logn) SC O(N**2)

        while len(visited) < n:
            dist, p1 = heapq.heappop(minHeap)
            if p1 in visited:
                continue
            visited.add(p1)
            cost += dist
            for p2 in range(n):
                if p1 != p2 and p2 not in visited:
                    heapq.heappush(minHeap, (distance(p1, p2), p2))
        return cost