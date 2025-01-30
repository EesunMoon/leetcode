class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque: store index (in decreasing order)
        # deque[0]: maximum number's index

        # T O(n) S O(n)
        
        queue = deque()
        l = 0 # left boundary
        res = []
        for r in range(len(nums)):
            # r: right boundary

            # making queue in decreasing order(value) before adding index in queue
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r) # store index

            # check queue is out of boundry
            if queue[0] < l:
                queue.popleft()
            
            # check sliding window size
            if (r-l+1) == k:
                res.append(nums[queue[0]])
                l+=1
        return res