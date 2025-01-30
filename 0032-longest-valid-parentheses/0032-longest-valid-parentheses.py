class Solution:
    def longestValidParentheses(self, s: str) -> int:
        openNum, closeNum = 0, 0
        res = 0

        for char in s:
            if char == "(":
                openNum += 1
            else:
                closeNum += 1
            
            if openNum == closeNum:
                res = max(res, openNum + closeNum)
            elif openNum < closeNum:
                # reset
                openNum, closeNum = 0, 0
        
        openNum, closeNum = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ")":
                closeNum += 1
            else:
                openNum += 1
            
            if closeNum == openNum:
                res = max(res, openNum + closeNum)
            elif openNum > closeNum:
                # reset
                openNum, closeNum = 0, 0
        return res