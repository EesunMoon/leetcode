class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # min heap + bfs
        if not nums1 or not nums2:
            return []
        
        H = [] # min heap
        res = []
        # find the minimum pair (nums1[i], nums2[0])
        for i in range(min(k, len(nums1))):
            heapq.heappush(H, (nums1[i]+nums2[0], i, 0))

        # find smallest k pairs
        while k > 0 and H:
            subSum, i, j = heapq.heappop(H)
            res.append([nums1[i], nums2[j]])
            k -= 1
            # next element
            if j+1 < len(nums2):
                heapq.heappush(H, (nums1[i]+nums2[j+1], i, j+1))
        return res

        
        """
        # TC O(n*m(logk)) SC O(k)
        maxHeap = [] # (sum, [pair])

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(maxHeap, (-(nums1[i]+nums2[j]), [nums1[i],nums2[j]]))

                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        
        return [pair for _, pair in maxHeap]
        """