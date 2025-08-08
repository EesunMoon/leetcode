class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # array -> 0~26 T O(n) S O(26)
        
        # edge case
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1
        
        for n in count:
            if n != 0:
                return False
        return True