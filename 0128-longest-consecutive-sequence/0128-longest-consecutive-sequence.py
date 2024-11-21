class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numSet = set(nums)
        longest = 0

        for num in nums:
            # check whether num is a starting number of not
            if num-1 not in numSet:
                length = 0
                while length + num in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest