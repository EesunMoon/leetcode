class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window
        # queue: decreasing order
        queue = deque() # store index, add, remove O(1)
        l = 0
        res = []
        for r in range(len(nums)):
            # make queue in decreasing order
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            # out of bound
            if queue[0] < l:
                queue.popleft()

            if (r-l+1) == k:
                res.append(nums[queue[0]])
                l += 1
        return res