class MedianFinder:

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if len(self.small) > len(self.large)+1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            return
        if self.large and -self.small[0] > self.large[0]:
            val1 = -heapq.heappop(self.small)
            val2 = heapq.heappop(self.large)
            heapq.heappush(self.small, -val2)
            heapq.heappush(self.large, val1)

    def findMedian(self) -> float:
        S, L = len(self.small), len(self.large)
        if (S+L) % 2 != 0:
            return float(-self.small[0])
        else:
            return float(-self.small[0] + self.large[0])/2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()