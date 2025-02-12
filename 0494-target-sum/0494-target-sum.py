class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #### DP - bottom up approach 
        # TC O(n*m) SC O(m) space optimization
        # in this algorithm, we only think about current dp array and prior dp array
        dp = defaultdict(int) # act as priorDP dp[curr_sum] = count
        dp[0] = 1 # base case
        for i in range(len(nums)):
            currDP = defaultdict(int) # current dp
            for curr_sum, count in dp.items():
                currDP[curr_sum-nums[i]] += count
                currDP[curr_sum+nums[i]] += count
            dp = currDP
        return dp[target]
        
        #### DP - bottom up approach
        # TC O(n*m) SC O(n*m)
        dp = [defaultdict(int) for _ in range(len(nums)+1)] # dp[index][curr_sum] = count
        dp[0][0] = 1 # base case
        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                dp[i+1][curr_sum-nums[i]] += count
                dp[i+1][curr_sum+nums[i]] += count
        return dp[len(nums)][target]
        
        #### DP - memoization approach
        # TC O(n*m) n: len(nums), m: sum(nums) SC O(n*m)
        dp = {} #(index, amount): the number of expressions

        def dfs(i, total):
            # base case
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i])
            return dp[(i, total)]
        return dfs(0, 0)
