class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ope = ['+', '-', '*', '/']
        stack = []

        for t in tokens:
            if t in ope:
                x = stack.pop()
                y = stack.pop()
                operation = str(eval(y + t + x))

                # The division between two integers always truncates toward zero
                if t == '/' and int(y) % int(x) != 0 and int(operation) < 0:
                    operation = str(int(operation) + 1)

                stack.append(operation)
            else:
                stack.append(t)
            
        
        return int(stack.pop())
        
        