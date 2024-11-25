class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total = 0
        n = len(height)-1
        maxl, maxr = height[0], height[n]

        l, r = 0, n
        while l<r:
            
            if maxl < maxr:
                l+=1
                maxl = max(maxl, height[l])
                total += maxl-height[l]
            else:
                r-=1
                maxr = max(maxr, height[r])
                total += maxr-height[r]
            
        return total