class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = len(nums)
        start = 1

        for i in range(t):
            start = i+1
            dups = 0
            for j in range(start, t):
                if nums[i] == nums[j]:
                    dups += 1
                else:
                    break
            nums[start:] = nums[start+dups:]
            i += dups
            t -= dups
                    
        return 
