class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build hashmap
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        # using heap
        H = []
        for num, freq in hashmap.items():
            heapq.heappush(H, (freq, num))
            if len(H) > k:
                heapq.heappop(H)

        res = []
        while H:
            freq, num = heapq.heappop(H)
            res.append(num)
        return res