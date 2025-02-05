class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        s = 'aab'
        i = 0 ~ 2
            -> aab
        TC O(N*2^N) SC O(N*N)
        """
        def isPal(l, r):
            while l<=r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        def backtracking(i, sub):
            # base case
            if i == len(s):
                res.append(sub.copy())
                return
            
            for j in range(i, len(s)):
                if isPal(i, j):
                    sub.append(s[i:j+1])
                    backtracking(j+1, sub)
                    sub.pop()
        
        backtracking(0, [])
        return res