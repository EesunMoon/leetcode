class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        longest = 0
        setnums = set(nums)

        for num in nums:
            if num-1 not in setnums:
                length = 1
                while num+length in setnums:
                    length += 1
                
                longest = max(longest, length)
        return longest

       