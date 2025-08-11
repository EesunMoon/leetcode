class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # finding the starting point
        res = 0
        setNums = set(nums)
        for num in setNums:
            # starting point?
            if not num-1 in setNums:
                length = 1
                while num + length in setNums:
                    length += 1
                res = max(length, res)
        return res
            