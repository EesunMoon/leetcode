class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if) sorting => O(nlogn)
        # solve without sorting

        longest = 0
        setnums = set(nums)

        for num in setnums:
            if (num-1) not in setnums: # starting point
                length = 1
                while (num + length) in setnums:
                    length += 1
                longest = max(longest, length)

        return longest