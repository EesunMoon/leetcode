class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        brute force: TC O(n**2) SC O(n**2)
            every subsequence O(n**2)
                compute sum -> store (length, sum)
        sliding window: TC O(n) SC O(1)
            l, r: starting from 0
            
            2, 3, 1, 2, 4, 3
                     l
                        r
            subSum 10
        """
        # base case
        if sum(nums) < target:
            return 0

        minLength = float("INF") # length: r - l + 1
        l, subSum = 0, 0
        for r in range(len(nums)):
            subSum += nums[r]

            # shring window size
            while l <= r and subSum >= target:
                minLength = min(minLength, r-l+1)
                subSum -= nums[l]
                l += 1
        return minLength if minLength != float("INF") else 0

        """
        # brute force: TC SC O(n**2) 
        combination = [] # [length, total sum]
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                subSum = sum(nums[start:end+1])
                combination.append([end-start+1, subSum])
        
        minLength = float("INF")
        for length, subSum in combination:
            if subSum >= target:
                minLength = min(minLength, length)
        return minLength if minLength != float("INF") else 0
        """