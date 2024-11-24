class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sorting => O(nlogn)
        # 1, 2, 3, 4, | 100, | 200

        setNums = set(nums)
        longest = 0

        for num in setNums:
            if (num-1) not in setNums: # starting point
                length = 1
                while (length + num) in setNums:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
        