class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = [] # current pair
        res = [] # overall pairs

        def backtrack(openN, closedN):
            # base case
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # add open parentheses
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

            # add closed parentheses
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        
        backtrack(0, 0)
        return res