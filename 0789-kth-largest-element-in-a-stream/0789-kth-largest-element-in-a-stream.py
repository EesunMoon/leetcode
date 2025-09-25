class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.track = []
        for num in nums:
            heapq.heappush(self.track, num)
            while len(self.track) > self.k:
                heapq.heappop(self.track)

    def add(self, val: int) -> int:
        heapq.heappush(self.track, val)
        if len(self.track) > self.k:
            heapq.heappop(self.track)
        return self.track[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)