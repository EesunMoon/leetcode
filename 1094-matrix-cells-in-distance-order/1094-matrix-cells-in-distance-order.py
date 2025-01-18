class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        H = []
        def dist(r, c):
            return abs(r-rCenter)+abs(c-cCenter)
        
        for r in range(rows):
            for c in range(cols):
                heapq.heappush(H, [dist(r,c), [r, c]])
        
        res = []
        while H:
            dist, cor = heapq.heappop(H)
            res.append(cor)
        return res