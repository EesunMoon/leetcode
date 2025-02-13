class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                while l <= r and k < 0:
                    k += 1 if nums[l] == 0 else 0
                    l += 1
            maxLen = max(maxLen, r-l+1)
        return maxLen