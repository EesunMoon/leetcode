class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        let's assume we want to make X
        (tops[i] == X or bottom[i] == X) or (tops[i]==X and bottoms[i] == X)
        candidates should be 2 or 1
            candidatates = tops[0], bottoms[0]
        check -> min(tops[i] != candidates, bottoms[i] != candidates)
        min(check(tops[0]), check(bottoms[0]))
        """
        n = len(tops)
        def check(candidate):
            numTops = 0
            numBottoms = 0
            for i in range(n):
                if tops[i] != candidate and bottoms[i] != candidate:
                    return float("INF") # invalid
                if tops[i] != candidate:
                    numTops += 1
                if bottoms[i] != candidate:
                    numBottoms += 1
            return min(numTops, numBottoms)
        
        cand1, cand2 = tops[0], bottoms[0]
        ans = min(check(cand1), check(cand2))
        return ans if ans != float("INF") else -1
