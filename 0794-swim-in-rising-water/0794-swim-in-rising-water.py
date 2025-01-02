class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        visited = set()
        visited.add((0, 0))
        minHeap = [(grid[0][0], 0, 0)] # maxTime, r, c
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == N-1 and c == N-1:
                return t
            
            for dr, dc in directions:
                candr, candc = dr + r, dc + c
                if candr in (-1, N) or candc in (-1, N) or (candr, candc) in visited:
                    continue
                visited.add((candr, candc))
                heapq.heappush(minHeap, (max(t, grid[candr][candc]), candr, candc))
