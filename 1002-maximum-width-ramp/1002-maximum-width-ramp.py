class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # width: j - i, nums[i] <= nums[j]
        # Q) maximum width of ramp
        """
        6 0 8 2 1 5
        l         r
        """
        
        stack = [] # decreasing
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        res = 0
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                res = max(res, j-i)
        return res