class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort by start
        intervals.sort(key=lambda x:x[0])
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # overlap
            if prevEnd > start:
                res += 1
                prevEnd = min(end, prevEnd)
                continue
            prevEnd = end

        return res