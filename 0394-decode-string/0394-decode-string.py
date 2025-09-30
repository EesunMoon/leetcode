class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                sub = ""
                while stack[-1] !="[":
                    sub = stack.pop() + sub
                stack.pop() # "["
                
                k = ""
                while stack and stack[-1] in "0123456789":
                    k = stack.pop() + k
                stack.append(sub*int(k))
            else:
                stack.append(c)
        return "".join(stack)
        