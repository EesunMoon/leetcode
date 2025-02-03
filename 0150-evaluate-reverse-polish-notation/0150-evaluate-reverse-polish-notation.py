class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token in "+-*/":
                t1 = stack.pop()
                t2 = stack.pop()
                if token == "+":
                    stack.append(t2+t1)
                elif token == "-":
                    stack.append(t2-t1)
                elif token == "*":
                    stack.append(t2*t1)
                elif token == "/":
                    stack.append(int(float(t2)/t1))
            else:
                stack.append(int(token))
        return stack[0]