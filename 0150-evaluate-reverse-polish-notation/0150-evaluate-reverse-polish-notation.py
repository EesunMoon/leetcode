class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                v = stack.pop()
                if t == "+":
                    stack[-1] += v
                elif t == "-":
                    stack[-1] -= v
                elif t == "*":
                    stack[-1] *= v
                else:
                    v2 = stack.pop()
                    val = abs(v2) // abs(v)
                    if v2*v < 0:
                        val *= -1
                    stack.append(val)
            else:
                stack.append(int(t))
        return stack[0]