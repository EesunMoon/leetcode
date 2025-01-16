class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            newDP = set()
            for t in dp:
                if t+nums[i] == target:
                    return True
                newDP.add(t)
                newDP.add(t+nums[i])
            dp = newDP
        return True if target in dp else False
                