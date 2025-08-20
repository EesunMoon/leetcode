import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # T O(nlog(max(piles))) S O(1)
        
        def calHours(k):
            total = 0
            for p in piles:
                total += ceil(float(p)/k)
            return total
        
        l, r = 1, max(piles) # O(n)
        res = r
        while l<=r:
            k = (l+r)//2
            cand = calHours(k)
            if cand > h:
                l = k+1
            else:
                res = min(k, res)
                r = k-1
        return res