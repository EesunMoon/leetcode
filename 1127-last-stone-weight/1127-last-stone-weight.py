class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        bucket = []
        for s in stones:
            heapq.heappush(bucket, -s)
        
        while len(bucket) > 1:
            y = -heapq.heappop(bucket)
            x = -heapq.heappop(bucket)
            if x != y:
                heapq.heappush(bucket, -(y-x))
        return -bucket[0] if bucket else 0