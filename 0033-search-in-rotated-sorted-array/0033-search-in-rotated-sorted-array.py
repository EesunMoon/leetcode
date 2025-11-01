class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            # typical binary search
            if nums[l]<=nums[r]:
                if nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[l] <= nums[m]: # left portion is sorted
                    if target > nums[m] or target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                else: # right portion is sorted 
                    if target < nums[m] or target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
        return -1