class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        total = len(nums)

        def helper(l, target):
            if l > total:
                return False
            if len(set(nums[l:])) == target:
                return True
            else:
                return False
        
        res = 0
        for i in range(0, total-1, 3):
            if helper(i, total-i):
                return res
            res += 1
        return res
        """

        count = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] not in count:
                count.add(nums[i])
            else:
                return i//3 + 1
        return 0