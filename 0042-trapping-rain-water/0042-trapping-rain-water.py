class Solution:
    def trap(self, height: List[int]) -> int:
        # area: min(letftMax, rightMax) - height[i]
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(height[l], leftMax)
                res += max(0, min(leftMax, rightMax) - height[l])
            else:
                r-= 1
                rightMax = max(height[r], rightMax)
                res += max(0, min(leftMax, rightMax) - height[r])
            
            
        return res
