class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # ocean is to the right of the buildings
        maxHeight = 0
        res = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxHeight:
                res.append(i)
            maxHeight = max(maxHeight, heights[i])
        return res[::-1]