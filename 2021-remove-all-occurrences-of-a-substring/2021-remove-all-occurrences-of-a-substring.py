class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        daabcbaabcbc, abc
            dabaabcbc -> dababc -> dab
        """
        stack = []
        target_length = len(part)
        target_end = part[-1]
        
        for c in s:
            stack.append(c)

            if c == target_end and len(stack) >= target_length:
                if "".join(stack[-target_length:]) == part:
                    del stack[-target_length:]
        return "".join(stack)

        

        