class Solution(object):
    def findKthLargest(self, nums, k):
        H = []

        for num in nums:
            heapq.heappush(H, num)
            if len(H) > k:
                heapq.heappop(H)

        return H[0]