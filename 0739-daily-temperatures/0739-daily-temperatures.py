class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        ex) [73,74,75,71,69,72,76,73]
        if stack[-1] < num => pop 
        stack : store index
        """
        # stack: with monotonic decreasing stack
        stack = [] # store index
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res