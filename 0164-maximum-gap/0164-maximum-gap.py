class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        maxVal = max(nums)
        exp = 1
        radix = 10
        sorted_nums = [0] * len(nums)
        
        while maxVal // exp > 0:
            # count
            count = [0]*radix
            for num in nums:
                count[(num//exp)%10] += 1
            # culmulative count
            prev = 0
            for i, cnt in enumerate(count):
                count[i] = prev
                prev += cnt
            
            for num in nums:
                sorted_nums[count[(num//exp)%10]] = num
                count[(num//exp)%10] += 1
            
            # copy sorted order to original
            nums = sorted_nums[:]
            exp *= 10
            

        max_diff = 0
        for i in range(len(nums)-1):
            max_diff = max(max_diff, nums[i+1] - nums[i])
        
        return max_diff