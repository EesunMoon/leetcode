class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.data = [0]*size
        self.size = size
        self.count = 0
        self.idx = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.data[self.idx] = val
        self.idx = (self.idx+1)%self.size
        if self.count != self.size:
            self.count += 1
        return sum(self.data) / float(self.count)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)