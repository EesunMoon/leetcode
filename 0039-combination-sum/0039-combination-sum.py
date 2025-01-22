class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(i, cand, total):
            # base case
            if total == target:
                res.append(cand[::])
                return
            if i >= len(candidates) or total > target:
                return
            
            cand.append(candidates[i])
            backtracking(i, cand, total + candidates[i])
            cand.pop()
            backtracking(i+1, cand, total)
        
        backtracking(0, [], 0)
        return res