class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        5, 7, 7, 8, 8, 10
        l               r
              m
        """
        def binary_search(isSearchingLeft):
            l, r = 0, len(nums)-1
            idx = -1

            while l<=r:
                m = (l+r)//2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    idx = m
                    if isSearchingLeft:
                        r = m - 1
                    else:
                        l = m + 1
            return idx 

        start = binary_search(True)
        end = binary_search(False)
        return [start, end]