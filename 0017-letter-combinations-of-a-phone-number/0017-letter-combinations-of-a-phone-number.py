class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            "2":"abc", "3":"def", "4":"ghi",
            "5":"jkl", "6":"mno", "7":"pqrs",
            "8":"tuv", "9":"wxyz"
        }

        res = []
        
        def dfs(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            for c in mapping[digits[i]]:
                dfs(i+1, curr+c)
        
        if digits:
            dfs(0, "")
        return res
