class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        points = [(r, c) for r in range(rows) for c in range(cols)]
        def dist(point):
            return abs(point[0]-rCenter)+abs(point[1]-cCenter)
        return sorted(points, key=dist)