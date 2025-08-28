class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic descreasing stack TC O(n) SC O(n)
        # dp TC O(n) SC O(1) <<< ...? how?

        stack = [] # [temp, idx]
        res = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                temp, idx = stack.pop()
                res[idx] = (i-idx)
            stack.append([val, i])
        return res