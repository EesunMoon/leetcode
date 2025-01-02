class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        intervals.sort(key=lambda x:x[0])
        endTime = intervals[0][1]
        for idx in range(1, len(intervals)):
            if endTime > intervals[idx][0]:
                return False
            endTime = intervals[idx][1]
        return True
        