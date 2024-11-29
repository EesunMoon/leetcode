class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = {len(s):1} # base case

        n = len(s)

        # bottom up approach
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            # 2-digit case
            if (i+1 < n):
                if (s[i] =="1" ) or (s[i]=="2" and s[i+1] in "0123456"):
                    dp[i] += dp[i+2]
        
        return dp[0]

