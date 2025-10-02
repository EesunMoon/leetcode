class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(searchLeft):
            l, r = 0, len(nums)-1
            point = -1
            while l<=r:
                m = l + (r-l)//2
                if nums[m] > target:
                    r = m-1
                elif nums[m] < target:
                    l = m + 1
                else:
                    point = m
                    if searchLeft:
                        r = m-1
                    else:
                        l = m+1
            return point
        left, right = binarySearch(True), binarySearch(False)
        return [left, right]
