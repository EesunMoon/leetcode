class Solution(object):
    def countDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        word = set()
        for i in range(N):
            for j in range(i+1, N+1):
                word.add(s[i:j])
        return len(word)
        