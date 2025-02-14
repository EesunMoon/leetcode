class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
            pbbcggttciiippooaais
            p
        """
        stack = [] # [char, continuous freq]
        for c in s:
            if stack and stack[-1][0] == c:
                ch, freq = stack.pop()
                if freq + 1 != k:
                    stack.append([ch, freq+1])
            else:
                stack.append([c, 1])
        return "".join(c * freq for c, freq in stack)