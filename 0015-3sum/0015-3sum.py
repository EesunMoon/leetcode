class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort
        nums.sort() # O(nlogn)
        result = []

        # the solution set must no contain duplicate triplets
        for k in range(len(nums)):
            # fixed nums[k]
            if k !=0 and nums[k]==nums[k-1]:
                continue
            
            i, j = k+1, len(nums)-1
            while i<j:
                triple = nums[k] + nums[i] + nums[j]
                if triple > 0:
                    j-=1
                elif triple < 0:
                    i+=1
                else:
                    result.append([nums[k], nums[i], nums[j]])
                    i+=1
                    while i<j and nums[i] == nums[i-1]:
                        i+=1
                    
        return result