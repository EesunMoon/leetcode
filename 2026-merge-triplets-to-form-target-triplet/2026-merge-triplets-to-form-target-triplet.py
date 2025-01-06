class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        good = set() # if good contains all index in target => true

        for t in triplets:
            # if one of elements in t is bigger than targets => skip
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
            
        return len(good) == len(target)