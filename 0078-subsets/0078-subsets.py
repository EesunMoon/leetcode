class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        subSet = []
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subSet[::])
                return
            
            # option 1) include nums[i]
            subSet.append(nums[i])
            dfs(i+1)

            # option 2) not include nums[i]
            subSet.pop()
            dfs(i+1)
        
        dfs(0)
        return res
        