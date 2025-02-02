class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
                
            if k < 0:
                while k < 0 and l <= r:
                    if nums[l] == 0:
                        k += 1
                    l += 1
            
            maxLen = max(maxLen, (r-l+1))
        return maxLen
            