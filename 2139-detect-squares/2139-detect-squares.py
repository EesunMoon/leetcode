class DetectSquares(object):

    def __init__(self):
        self.square = defaultdict(int)
        self.pts = []

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.square[tuple(point)] += 1
        self.pts.append(point)
        
    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        res = 0
        px, py = point
        for x, y in self.pts:
            # check diagnal points
            if (abs(px-x)!=abs(py-y)) or px == x or py ==y:
                continue
            
            # other points
            res += self.square[(px, y)] * self.square[(x, py)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)