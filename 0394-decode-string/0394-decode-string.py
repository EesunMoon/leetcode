class Solution:
    def decodeString(self, s: str) -> str:
        # 1. [: finish digit, start s (digit shoud come out until [, after [, alpha will come out)
        # 2. ]: can make the encoded string using stack (digitstack, strstack)

        
        # if c.isdigit(): digit = digit*10+int(c)
        # if c == "[", append digit into digit-stack and init sub="" and digit, append sub into sub-stack
        # if c == "]", digit pop, subsub = sub, 
        # if c.isalpha(): sub += c
        
        k_stack, str_stack = [], []
        k, curr = 0, ""

        for c in s:
            if c.isdigit():
                k = k*10 + int(c)
            elif c == "[":
                k_stack.append(k); k = 0 # finish k
                str_stack.append(curr); curr = "" # start sub
            elif c == "]":
                sub = curr
                curr = str_stack.pop()
                cnt = k_stack.pop()
                curr += (sub*cnt)
            else:
                curr += c
        return curr