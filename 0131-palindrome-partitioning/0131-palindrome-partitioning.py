class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def isPalindrom(l, r):
            while l<=r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(i, cand):
            if i == len(s):
                res.append(cand[::])
                return
            for j in range(i, len(s)):
                if isPalindrom(i, j):
                    cand.append(s[i:j+1]) # partition
                    dfs(j+1, cand) # next character
                    cand.pop()
        
        dfs(0, [])
        return res


        