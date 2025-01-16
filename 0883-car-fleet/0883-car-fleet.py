class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # phase 1) sorted by position in decreasing order
        # -> make sure largest position first
        pair = [[p, s] for p, s in zip(position, speed)]

        # phase 2) compute car fleet using arrived time
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/float(s))

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)