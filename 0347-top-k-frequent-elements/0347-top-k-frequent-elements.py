class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # 1) hashmap => O(n)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        # 2) heapify
        heap = []
        for nums, freq in count.items():
            heapq.heappush(heap, (freq, nums))

            if len(heap) > k:
                heapq.heappop(heap)
        
        # 3) result
        res = []
        for i in range(k):
            freq, ele = heapq.heappop(heap)
            res.append(ele)
        
        return res
