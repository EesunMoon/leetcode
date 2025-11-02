class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = 0, float("-inf")
        for n in nums:
            currSum += n
            if maxSum < currSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return maxSum