class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # koko can eat a piles in a hour
        # return minimum
        # search range: [1, ..., max(piles)]

        l, r = 1, max(piles)
        k = r

        while l<=r:
            cand = (l+r)//2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/cand)
            
            if hours <= h:
                k = min(k, cand)
                r = cand-1
                
            else:
                l = cand+1
        
        return k