class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def dfs(i, curr):
            if i == len(nums):
                res.append(curr[::])
                return
            if i > len(nums):
                return
            
            # include value
            curr.append(nums[i])
            dfs(i+1, curr)

            # not include value
            curr.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1, curr)
        
        dfs(0, [])
        return res