class Solution(object):
    def countDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                a.append(s[i:j])
        return len(set(a))
        