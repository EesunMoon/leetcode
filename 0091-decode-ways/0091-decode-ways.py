class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {len(s):1}

        # 11106
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                # 1-digit case
                dp[i] = dp[i+1]
            
            # 1-digit case
            if ((i+1 < len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"))):
                dp[i] += dp[i+2]
        
        return dp[0]