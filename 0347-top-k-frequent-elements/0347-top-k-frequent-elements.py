class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num: count
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        minHeap = [] # [freq, num]
        for n, freq in count.items():
            heapq.heappush(minHeap, [freq, n])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [ v for _, v in minHeap]