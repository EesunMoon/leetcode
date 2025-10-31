class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(2**target)
        res = []
        candidates.sort()

        def dfs(i, curr, cand):
            if curr == target:
                res.append(cand.copy())
                return # find
            if curr > target:
                return # invalid
            
            for j in range(i, len(candidates)):
                cand.append(candidates[j])
                dfs(j, curr + candidates[j], cand)
                cand.pop()
        
        dfs(0, 0, [])
        return res
