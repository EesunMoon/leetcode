class Solution(object):
    def lastStoneWeight(self, stones):
        maxHeap = []

        if len(stones) == 1:
            return stones[0]

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while maxHeap:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if x < y:
                heapq.heappush(maxHeap, -abs(y-x))
            
            if len(maxHeap) == 1:
                return -maxHeap[0]
        
        return 0