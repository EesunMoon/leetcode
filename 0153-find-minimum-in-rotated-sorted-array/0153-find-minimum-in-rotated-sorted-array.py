class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        
        while l<=r:
            # base case
            if nums[l]<nums[r]:
                res = min(res, nums[l])
                break
            else:
                m = (l+r)//2
                res = min(res, nums[m]) # check and save medium

                if nums[l]<=nums[m]:
                    res = min(res, nums[l])
                    l = m+1
                else:
                    r = m-1
        return res