class Solution:
    def isValid(self, s: str) -> bool:
        # base case: length - odd number -> false
        if len(s) % 2 != 0:
            return False
        
        stack = []
        pair = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in "])}":
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack
            