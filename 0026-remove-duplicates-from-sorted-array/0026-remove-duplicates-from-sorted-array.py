class Solution(object):
    def removeDuplicates(self, nums):
        l = 1 # l: represent the position that we replace
        # r: compare previous value and current value
        for r in range(1, len(nums)):
            # find distinct
            if nums[r-1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l


            

    '''
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
            print(nums)
                    
        return start
    '''