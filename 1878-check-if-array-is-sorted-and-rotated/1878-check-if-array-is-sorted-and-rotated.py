class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0 # rotate position
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]:
                cnt += 1
        return (cnt == 0) or (cnt == 1)