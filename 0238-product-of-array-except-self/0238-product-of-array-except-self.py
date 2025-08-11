class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        
        ans = []
        for n in nums:
            ans.append(prefix)
            prefix *= n
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= prefix
            prefix *= nums[i]
        return ans
