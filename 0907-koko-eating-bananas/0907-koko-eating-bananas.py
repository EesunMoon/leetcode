import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search: 1 ~ max(piles)
        # expected complexity: T O(nlogm) S O(1) n: len(piles), m: max(piles)
        
        # set the binary search boundary
        l, r = 1, max(piles) # O(n)
        res = r # minimum integer

        while l<=r:
            k = (l+r)//2 # amount

            # compute the time => O(n)
            take = 0 # time
            for p in piles:
                take += math.ceil(p/float(k))
            
            # binary search
            if take > h:
                # k is too small to eat all bananas in h
                l = k + 1
            else:
                # k is big enough to eat all bananas in h
                # find smallest value in this range
                res = min(res, k)
                r = k - 1
        return res