class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp = [0 for _ in range(len(text2)+1)]

        for i in range(len(text1)-1, -1, -1):
            newDP = [0 for _ in range(len(text2)+1)]
            for j in range(len(text2)-1, -1, -1):
                # if match -> previous diagnal dp + 1
                if text1[i] == text2[j]:
                    newDP[j] = 1 + dp[j+1]
                # do not match -> max(previous down dp, current right dp)
                else:
                    newDP[j] = max(dp[j], newDP[j+1])
            dp = newDP
        return dp[0]