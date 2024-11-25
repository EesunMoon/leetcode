class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # height = min(height[l], height[r])
        # width = abs(r-l)

        l, r = 0, len(height)-1 # max width
        maxamount = 0
        
        while l<r:
            w = abs(r-l)
            h = min(height[l], height[r])
            area = w*h
            maxamount = max(maxamount, area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxamount
