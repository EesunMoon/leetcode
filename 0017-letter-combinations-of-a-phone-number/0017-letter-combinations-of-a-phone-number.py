class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {"2":"abc", "3":"def", "4":"ghi",
                  "5":"jkl", "6":"mno", "7":"pqrs",
                  "8":"tuv", "9":"wxyz"}
        res = []
        def backtracking(i, cand):
            if len(cand) == len(digits):
                res.append(cand)
                return
            
            
            for c in letter[digits[i]]:
                backtracking(i+1, cand+c)
        if digits:
            backtracking(0, "")
        return res