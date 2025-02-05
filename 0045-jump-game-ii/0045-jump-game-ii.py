class Solution:
    def jump(self, nums: List[int]) -> int:
        # track how breath
        l, r = 0, 0 # left boundary of level, right boundary of level
        level = 0
        while r < len(nums)-1:
            furthest = 0
            for i in range(l, r+1):
                furthest = max(furthest, nums[i]+i)
            l = r + 1
            r = furthest
            level += 1
        return level
        # DP : variable index state the numbere of jumps
        # T O(n*m) S O(n)
        """
        dp = [float("INF")] * (len(nums))
        dp[len(nums)-1] = 0 # goal

        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i], 0, -1):
                if i + j >= len(nums):
                    dp[i] = 1
                    break
                dp[i] = min(dp[i], 1 + dp[i+j])
        return dp[0]
        """
        # optimize - Greedy O(n)
        # focus on how furthest jump at each level (total level = total step)
        
        l, r = 0, 0 # indicate level range (base case: 0th level)
        step = 0
        
        while r < len(nums)-1:
            # how furthest jump at each level
            furthest = 0
            for i in range(l, r+1):
                furthest = max(furthest, i + nums[i])
            
            # set next level range
            l = r + 1
            r = furthest
            step += 1

        return step
            