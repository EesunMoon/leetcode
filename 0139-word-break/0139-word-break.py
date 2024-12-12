class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # DSA: DP
        # idx : #. string
        # state: possible or not => True, False
        # recurrence variable: True, False

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]

        # S O(s) s: length of the string
        # T O(s*w) w: #.of the wordDict
