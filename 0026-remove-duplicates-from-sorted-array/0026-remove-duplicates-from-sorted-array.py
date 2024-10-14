class Solution(object):
    def removeDuplicates(self, nums):
        start = 1
        n = len(nums)

        # condition) it is guaranteed that the given array is a sorted array
        for i in range(1, n):
            # find unique element
            if nums[i-1] != nums[i]:
                nums[start] = nums[i]
                start += 1
        return start
            

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