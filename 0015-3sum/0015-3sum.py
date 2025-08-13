class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        do not contain duplicate triplets
        """
        nums.sort()
        N = len(nums)
        res = []

        for i in range(N-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, N-1

            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1

        return res
            