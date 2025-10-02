class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N-1
        
        while l<=r:
            m = l + ((r-l)//2)
            # left neighbor greater
            if m+1 < N and nums[m] < nums[m+1]:
                l = m + 1
            # left neighbor greater
            elif m-1 >= 0 and nums[m] < nums[m-1]:
                r = m - 1
            else:
                return m
