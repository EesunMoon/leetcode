class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # hashmap
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        
        l = 0
        res = []
        target = set()
        for r in range(len(s)):
            count[s[r]] -= 1
            target.add(s[r])
            flag = True
            for c in target:
                if count[c] != 0:
                    flag = False
                    break
            if flag:
                res.append(r-l+1)
                l = r+1
                target = set()
        return res