class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # O(nlong)

        n = len(nums)
        result = []

        for k in range(n):
            # prevent duplicates
            if k > 0 and nums[k-1] == nums[k]:
                continue
            
            i, j = k+1, n-1
            while i<j:
                cand = nums[i] + nums[j] + nums[k]
                if cand > 0:
                    j -= 1
                elif cand < 0:
                    i += 1
                else:
                    result.append([nums[k], nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i-1] and i<j:
                        i+= 1
        return result
            