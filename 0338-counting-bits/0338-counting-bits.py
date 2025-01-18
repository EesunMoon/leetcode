class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def cnt(n):
            res = 0
            while n:
                n, curr = divmod(n, 2)
                if curr == 1:
                    res += 1
            return res
        res = []
        for i in range(n+1):
            res.append(cnt(i))
        return res
        