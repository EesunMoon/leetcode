class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1) only add open parenthesis if open < n
        # 2) only add closing parenthesis if closed < open
        # 3) valid IF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            # valid case
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # add open parenthesis condition
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            
            # add closing parethesis condition
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0, 0)
        return res