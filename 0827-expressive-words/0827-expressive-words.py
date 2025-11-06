class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def isStretchy(word):
            if len(word) > len(s):
                return False
            l1, r1 = 0,0 # track word
            l2, r2 = 0,0 # track stretch
            while r1 < len(word) and r2 < len(s):
                if word[l1] != s[l2]:
                    return False
                
                # group
                while (r1+1) < len(word) and word[r1] == word[r1+1]:
                    r1 += 1
                while (r2+1) < len(s) and s[r2] == s[r2+1]:
                    r2 += 1
                group1, group2 = r1-l1+1, r2-l2+1

                if (group1 == group2) or (group1<group2 and group2 >=3):
                    r1 += 1
                    r2 += 1
                    l1 = r1
                    l2 = r2
                else:
                    return False

            return True if r1 == len(word) and r2 == len(s) else False
        res = 0
        for word in words:
            if isStretchy(word):
                res += 1
        return res