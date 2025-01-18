class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        
        # base case
        if total % 2:
            return False
        
        target = total // 2
        dp = set( ) # contain all available sum
        dp.add(0)
        for num in nums:
            tmp = set()
            for d in dp:
                if d + num == target:
                    return True
                tmp.add(d+num)
                tmp.add(d)
            dp = tmp
        return True if target in dp else False
        

        
                