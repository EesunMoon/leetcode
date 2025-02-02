class Solution:
    def calculate(self, s: str) -> int:
        # +, - add stack
        # * / pop calculate with next 
        # edge case: 0, more than 2 digits

        l, r = 0, 0
        stack = []
        ope = None
        s.replace(" ", "")
        print(s)
        while r < len(s):
            while r < len(s) and s[r] not in "+-/*":
                r += 1
            
            val = int(s[l:r])
            if not ope or ope == "+":
                stack.append(val)
            elif ope == "-":
                stack.append(-val)
            elif ope == "*":
                ex = stack.pop()
                stack.append(ex*val)
            elif ope == "/":
                # handling negative
                ex = stack.pop()
                if ex < 0:
                    stack.append((abs(ex)//val)*(-1))
                else:
                    stack.append(ex//val)

            ope = s[r] if r < len(s) else None
            l = r + 1
            r = l
        
        return sum(stack)