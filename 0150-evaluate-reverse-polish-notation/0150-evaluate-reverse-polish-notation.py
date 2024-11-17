class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import operator
        operations = {
            "+": lambda x, y: x+y,
            "-": lambda x, y: x-y,
            "*": lambda x, y: x*y,
            '/': lambda x, y: int(operator.truediv(x,y)) # truncate towards zero
        }
        stack = []

        for t in tokens:
            if t in operations:
                y = stack.pop()
                x = stack.pop()
                result = operations[t](x,y)
                stack.append(result)
            else:
                stack.append(int(t))
            
        
        return stack[-1]
        
        