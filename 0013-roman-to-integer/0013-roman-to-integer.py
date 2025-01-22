class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I":1, "V":5, "X":10, "L":50,
                    "C":100, "D":500, "M":1000}
        # IV, IX, XL, XC, CD, CM
        i, res = 0, 0
        while i<len(s):
            if (i+1 < len(s) and hashmap[s[i]] < hashmap[s[i+1]]):
                res += (hashmap[s[i+1]]-hashmap[s[i]])
                i += 2
            else:
                res += hashmap[s[i]]
                i += 1
        return res