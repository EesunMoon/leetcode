class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)
        for i, h in enumerate(heights):
            start=i # to store starting index that can be extended
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index)) # renew maxArea
                start = index
            stack.append([start, h])
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea