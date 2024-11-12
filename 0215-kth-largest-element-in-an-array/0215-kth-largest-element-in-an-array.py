class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # kth largest element - construct min heap 
        min_heap = []
        
        for num in nums:
            if len(min_heap) == k:
                if num > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
            else:
                heapq.heappush(min_heap, num)

        return min_heap[0]