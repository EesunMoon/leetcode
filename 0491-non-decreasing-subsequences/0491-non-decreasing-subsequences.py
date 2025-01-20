class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()

        def backtracking(i, curr):
            if i == len(nums):
                if len(curr) >= 2:
                    res.add(tuple(curr))
                return
            
            if not curr or curr[-1] <= nums[i]:
                curr.append(nums[i])
                backtracking(i+1, curr)
                curr.pop()
            backtracking(i+1, curr)
        
        backtracking(0, [])
        return [can for can in res]
        