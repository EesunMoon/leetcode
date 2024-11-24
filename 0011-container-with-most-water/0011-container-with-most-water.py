class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # height = min(height[l], height[r])
        # width = abs(r-l)
        maxAmount = 0

        l, r = 0, len(height)-1 # maximize the width
        while l<r:
            amount = abs(r-l) * min(height[l], height[r])
            maxAmount = max(maxAmount, amount)

            # maximize the height
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        
        return maxAmount