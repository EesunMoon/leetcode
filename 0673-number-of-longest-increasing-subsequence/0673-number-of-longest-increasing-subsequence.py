class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[i] < length[j]+1:
                        length[i] = length[j]+1
                        count[i] = 0
                    if length[i] == length[j]+1:
                        count[i] += count[j]
        
        max_length = max(length)
        result = 0
    
        for i in range(n):
            if length[i]==max_length:
                result += count[i]

        return result