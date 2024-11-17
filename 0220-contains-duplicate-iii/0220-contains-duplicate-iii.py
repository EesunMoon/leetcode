from sortedcontainers import SortedList

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        window = SortedList()
        # print(window)
        for i in range(len(nums)):
            idx = window.bisect_left(nums[i])
            # print(idx, window)
            
            # successor
            if idx != len(window) and window[idx] <= nums[i] + valueDiff:
                return True
            
            # predecessor
            if idx > 0 and window[idx-1] >= nums[i] - valueDiff:
                return True
            
            window.add(nums[i])
            if len(window) > indexDiff:
                window.remove(nums[i-indexDiff])
            
        return False
        