class MedianFinder(object):
    # Two heap => reduce time complexity n/2
    def __init__(self):
        self.small = [] # the smaller half of the list, max_heap
        self.large = [] # the larger half of the list, min_heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()