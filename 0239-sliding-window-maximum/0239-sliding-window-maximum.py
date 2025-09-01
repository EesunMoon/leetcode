class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        l = 0

        for r in range(len(nums)):
            # monotonic decreasing queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # shirink window: remove leftmost value
            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1

        return res