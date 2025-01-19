class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[::])
                return

            # invalid
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i]) # contain current num
            curr.pop()
            dfs(i+1, curr, total) # do not contain current num, contain next num
        
        dfs(0, [], 0)
        return res