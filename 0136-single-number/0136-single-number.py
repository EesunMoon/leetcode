class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # XOR: if a, b is same == 1
        res = 0 # 0 ^ n = n

        for num in nums:
            res = res ^ num
            print(res)
        return res