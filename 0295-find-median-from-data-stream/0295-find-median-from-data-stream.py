class MedianFinder:

    def __init__(self):
        self.small = [] # maxHeap, equal or one more elem than maxHeap
        self.large = [] # minHeap

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
            if len(self.large) > len(self.small):
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, -val)
        else:
            heapq.heappush(self.small, -num)
            if len(self.small)-len(self.large) > 1:
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        total = len(self.small) + len(self.large)
        if total % 2 != 0:
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()