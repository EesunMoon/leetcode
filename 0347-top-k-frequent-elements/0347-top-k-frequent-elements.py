class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # build hashmap: calculate frequencies => O(n)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # build heap (freq, num) => O(nlogk)
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # make result => O(k)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result