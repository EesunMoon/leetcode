class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        nums.sort() # O(nlogn)

        # the solution set must not contain duplicate triplets

        for k in range(len(nums)):
            if k >0 and nums[k] == nums[k-1]:
                continue
            
            i, j = k+1, len(nums)-1
            while i<j:
                candidate = nums[k] + nums[i] + nums[j]

                if candidate < 0:
                    i += 1
                elif candidate >0:
                    j-=1
                else:
                    result.append([nums[k], nums[i], nums[j]])
                    i+=1
                    while i<j and nums[i] == nums[i-1]:
                        i+=1
        return result