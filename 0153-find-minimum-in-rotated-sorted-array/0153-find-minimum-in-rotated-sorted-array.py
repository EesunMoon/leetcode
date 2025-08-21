class Solution:
    def findMin(self, nums: List[int]) -> int:
        # <<<<< rotation point(>) <<<<
        res = nums[0]
        l, r = 0, len(nums)-1

        while l<=r:
            # already sort
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r)//2
            res = min(res, nums[m]) # intermediate save
            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1 # search left portion
        return res