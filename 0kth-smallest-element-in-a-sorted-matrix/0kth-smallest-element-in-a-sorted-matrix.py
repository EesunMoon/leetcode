class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        min_heap = []
        for i in range(min(n, k)):
            min_heap.append((matrix[i][0], i, 0)) # value, row, col
        
        heapq.heapify(min_heap)

        while k:
            value, row, col = heapq.heappop(min_heap)
            if col < n-1:
                heapq.heappush(min_heap, (matrix[row][col+1], row, col+1))
            k-=1

        return value