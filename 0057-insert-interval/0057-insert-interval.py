class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # newEnd < start
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                # end < newStart
                res.append(intervals[i])
            else:
                # overlap - update newInterval
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res
        