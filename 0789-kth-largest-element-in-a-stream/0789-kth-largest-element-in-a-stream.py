class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.stream = nums
        heapq.heapify(self.stream)
        while len(self.stream) > k:
            heapq.heappop(self.stream)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.stream, val)
        if len(self.stream) > self.k:
            heapq.heappop(self.stream)
        return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)