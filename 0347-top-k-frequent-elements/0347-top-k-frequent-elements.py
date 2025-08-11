class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        """
        max heap
        T O(nlogn) S O(n)
        for n in nums:
            hashmap[n] -= 1 # make max heap

        heap = []
        for key, values in hashmap.items():
            heapq.heappush(heap, [values, key])
        ans = []
        for i in range(k):
            count, val = heapq.heappop(heap)
            ans.append(val)
        return ans
        """
        # min heap T O(klogk) O(n)
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        heap = []
        for key, values in hashmap.items():
            heapq.heappush(heap, [values, key])
            while len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        while heap:
            count, val = heapq.heappop(heap)
            ans.append(val)
        return ans