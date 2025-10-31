class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(2**target)
        res = []
        candidates.sort()

        def dfs(i, curr, cand):
            if curr == target:
                res.append(cand.copy())
                return # find
            if i >= len(candidates) or curr > target:
                return # invalid
            
            # first decision - include current value
            cand.append(candidates[i])
            dfs(i, curr+candidates[i], cand)
            # other decision - not include
            cand.pop()
            dfs(i+1, curr, cand)
        
        dfs(0, 0, [])
        return res
