class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # T O(n) S O(1)
        
        setNums = set(nums)
        LCS = 0

        for num in setNums:
            # check starting number
            if (num-1) not in setNums:
                length = 1
                while (num + length) in setNums:
                    length += 1
                LCS = max(LCS, length)
        return LCS