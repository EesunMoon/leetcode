class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height)-1
        cnt = 0
        maxL, maxR = 0, 0

        while l<=r:
            if maxL <= maxR:
                num = min(maxL, maxR) - height[l]
                cnt += num if num>0 else 0
                maxL = max(height[l], maxL)
                l += 1
            else:
                num = min(maxL, maxR) - height[r]
                cnt += num if num > 0 else 0
                maxR = max(height[r], maxR)
                r -= 1
        return cnt

        