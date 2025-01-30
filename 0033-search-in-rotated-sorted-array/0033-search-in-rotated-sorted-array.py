class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        l, r = 0, len(nums)-1
        
        # sorted - regular binary search
        if nums[l] < nums[r]:
            while l<=r:
                m = (l+r) // 2
                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    l = m + 1 # search right portion
                else:
                    r = m - 1 # search left portion
        # rotated
        else:
            while l<=r:
                m = (l+r)//2
                
                if nums[m] == target:
                    return m
                
                # left portion
                if nums[m] >= nums[l]:
                    if target < nums[m] and target >= nums[l]:
                        r = m - 1
                    else:
                        l = m + 1
                # right portion
                else:
                    if target > nums[m] and target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
        return -1 # not found
