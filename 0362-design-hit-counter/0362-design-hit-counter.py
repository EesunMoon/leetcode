class HitCounter:
    # in chronological order
    def __init__(self):
        self.hits = deque([])
        self.total = 0
        
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp) # monotonically increasing
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        """ (timestamp-300) ~ (timestamp) """
        while (self.hits) and (self.hits[0] <= timestamp-300): 
            self.hits.popleft()
            self.total -= 1
        return self.total
        



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)