class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        # two pointer => T O(n), S O(1)
        l, r = 0, len(height)-1

        while l<r:
            # calculate another value
            w, h = (r-l), min(height[l], height[r])
            res = max(res, w*h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res