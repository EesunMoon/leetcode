class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # reduce space complexity: set text that has smaller size length as text2
        # TC O(n*m) SC O(m)
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        dp = [0] * (len(text1)+1) # act as prior dp
        for i in range(len(text1)-1, -1, -1):
            newDP = [0] * (len(text2)+1) # current DP
            for j in range(len(text2)-1, -1, -1):
                # 1) matches: diagnal + 1
                if text1[i] == text2[j]:
                    newDP[j] = dp[j+1] + 1
                # 2) not matches: right(current DP), down(prior DP)
                else:
                    newDP[j] = max(newDP[j+1], dp[j]) # max(right, down)
            dp = newDP
        return dp[0]