class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # build max heap
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        for _ in range(k):
            element = heapq.heappop(heap)

        return -element