class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, cand):
            if curr == target:
                res.append(cand.copy())
                return
            if i >= len(candidates) or curr > target:
                return

            cand.append(candidates[i])
            dfs(i, curr+candidates[i], cand)
            cand.pop()
            dfs(i+1, curr, cand)
        
        dfs(0, 0, [])
        return res
