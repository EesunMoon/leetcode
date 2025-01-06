class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # hashmap
        count = {}
        for i, c in enumerate(s):
            count[c] = i
        
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, count[c])

            if i == end:
                res.append(size)
                size = 0
        return res