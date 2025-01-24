class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # edge case
        if finalSum % 2:
            return []
        
        # greedy
        res = []
        
        total, i = 0, 1
        while total <= finalSum:
            total += (i*2)
            res.append(i*2)
            i += 1
        
        sub = total - finalSum
        res.remove(sub)
        return res
                