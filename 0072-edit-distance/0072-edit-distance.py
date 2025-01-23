class Solution:
    """
            same: (i+1, j+1)
            differ: (1) insert: 1+ (i+1, j)
                    (2) delete: 1+ (i, j+1)
                    (3) replace: 1+ (i+1, j+1)
    """
    # using bottom-up approach
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("INF")] * (len(word2)+1) for _ in range(len(word1)+1)]
        
        # base case
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        return dp[0][0]
    """
    # using top-down DP approach
    # time: O(m+n), space: O(m+n)
    def minDistance(self, word1: str, word2: str) -> int:
        
        cache = {}
        def dfs(i, j):
            # base case
            if i == len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i

            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i+1, j+1)
            else:
                cache[(i, j)] = 1 + min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
        
            return cache[(i, j)]
        return dfs(0,0)
    """