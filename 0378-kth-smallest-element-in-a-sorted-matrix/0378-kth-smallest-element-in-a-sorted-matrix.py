class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # add first element in matrix with index (value, (r, c))
        n = len(matrix)
        H = [[matrix[r][0], [r, 0]] for r in range(len(matrix))] # O(N)
        heapq.heapify(H) # O(NlogN)

        # O(klogN)
        for _ in range(k):
            val, coor = heapq.heappop(H)
            if coor[1] != n-1:
                heapq.heappush(H, [matrix[coor[0]][coor[1]+1], [coor[0], coor[1]+1]])
        return val