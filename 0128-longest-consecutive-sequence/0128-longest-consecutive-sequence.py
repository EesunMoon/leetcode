class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        setNum = set(nums)
        for num in setNum:
            
            if num-1 not in setNum: # starting point
                length = 1
                while length + num in setNum:
                    length += 1
                res = max(res, length)
        return res
            