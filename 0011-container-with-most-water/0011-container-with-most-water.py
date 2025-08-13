class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height * width
        # height: min(height[l], height[r]), width: r-l
        # BF T O(n**2) | two pointer T O(n) S O(1)
        
        l, r = 0, len(height)-1
        res = 0
        while l<r:
            w = r-l
            h = min(height[l], height[r])
            res = max(res, w*h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res