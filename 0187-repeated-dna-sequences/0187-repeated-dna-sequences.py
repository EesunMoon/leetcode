class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
            edge case) len(s) < 10 -> None
            A:0, C:1, G:2, T:3
        """
        # base case
        if len(s) < 10:
            return []
        
        seen = set()
        repeated = set()
        for i in range(len(s)-9):
            cand = s[i:i+10]
            if cand in seen:
                repeated.add(cand)
            seen.add(cand)
        return list(repeated)


