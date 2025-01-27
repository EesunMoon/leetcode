class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        setNums = set(nums) 
        # have to convert except for zero
        if 0 in setNums:
            setNums.remove(0)
        return len(setNums)