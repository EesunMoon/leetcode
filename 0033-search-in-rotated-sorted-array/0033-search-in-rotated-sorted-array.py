class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l<=r:
            m = (l+r)//2
            if nums[m] == target: # base case
                return m 
            if nums[l] < nums[r]: # standard
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else: # rotate case
                if nums[l] <= nums[m]:
                    if (nums[m] > target) and (nums[l] <= target):
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if (nums[m] < target) and (target <= nums[r]):
                        l = m + 1
                    else:
                        r = m - 1
        return -1