class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            flag = True
            while stack and stack[-1] == c:
                t = stack.pop()
                flag = False
            if flag:
                stack.append(c)

        return "".join(stack)
