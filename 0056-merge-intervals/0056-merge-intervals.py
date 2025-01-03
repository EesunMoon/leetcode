class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sorting by start => O(nlogn)
        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]
        for start, end in intervals[1:]:
            LastEnd = res[-1][1]
            if LastEnd < start:
                res.append([start, end])
            else:
                res[-1][1] = max(LastEnd, end)
        return res