class Solution(object):
    def removeDuplicates(self, nums):
        pos = 1 # add position <=> #. unique elements
        idx = 1 # moving pointer
        while idx  < len(nums):
            if nums[idx] != nums[idx-1]:
                nums[pos] = nums[idx]
                pos += 1
            
            idx += 1

        return pos
            

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