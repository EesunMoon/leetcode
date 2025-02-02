class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sorting
        nums.sort()
        return nums[len(nums)//2]