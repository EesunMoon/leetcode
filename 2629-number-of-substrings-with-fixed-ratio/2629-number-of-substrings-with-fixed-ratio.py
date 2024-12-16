class Solution(object):
    def fixedRatio(self, s, num1, num2):
        """
        :type s: str
        :type num1: int
        :type num2: int
        :rtype: int
        """
        ans = 0
        vis = defaultdict(int)
        vis[0] = 1
        a, b = 0, 0

        for x in s:
            if x == "1":
                b += 1
            else:
                a += 1
        
            ans += vis[a*num2-b*num1]
            vis[a*num2-b*num1] += 1

        return ans