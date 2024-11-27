class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles) # O(n)
        minamount = r

        while l<=r:
            m = (l+r)//2
            
            total = 0
            for pile in piles:
                total += math.ceil(float(pile)/m)

            if total > h:
                l = m+1
            else:
                minamount = min(minamount, m)
                r = m-1
        
        return minamount