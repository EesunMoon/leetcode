class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # stack
        stacks = []
        stackt = []

        for c in s:
            if c == "#":
                if stacks:
                    stacks.pop()
            else:
                stacks.append(c)
        
        for c in t:
            if c == "#":
                if stackt:
                    stackt.pop()
            else:
                stackt.append(c)

        # print(stacks, stackt)
        return ''.join(stacks) == ''.join(stackt)
        