class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        if x < 2:
            return 1
        
        l, r = 2, x//2

        while l <= r:
            pivot = l + (r-l)//2
            target = pivot * pivot
            if target > x:
                r = pivot - 1
            elif target < x:
                l = pivot + 1
            else:
                return pivot
        return r