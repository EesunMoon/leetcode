class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = [] # [index, height]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackIdx, stackHei = stack.pop()
                maxArea = max(maxArea, stackHei*(i-stackIdx)) # calculare prior area
                start = stackIdx
            
            stack.append((start, h))
        
        # remain stack
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea
        