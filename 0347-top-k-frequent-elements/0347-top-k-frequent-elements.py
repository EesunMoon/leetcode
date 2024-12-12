class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # hashmap => key: freq O(n) n: #.of nums
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        # top k freq elements O(nlogk)
        q = []
        for n, freq in hashmap.items():
            heapq.heappush(q, [freq, n])
            if len(q) > k:
                heapq.heappop(q)
        
        # make answer O(klogk)
        answer = []
        for _ in range(k):
            freq, n = heapq.heappop(q)
            answer.append(n)
        return answer