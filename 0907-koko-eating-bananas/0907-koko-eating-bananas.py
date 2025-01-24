import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # base case
        if len(piles) == h:
            return max(piles)

        l, r = 1, max(piles) # range: amount of banana to eat for a one
        res = r

        while l<=r:
            m = (l+r)//2

            cand = 0 # candidate hour
            for p in piles:
                cand += math.ceil(p/float(m))
            
            if cand <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
