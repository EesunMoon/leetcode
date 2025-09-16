class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        endTime = float("-inf")
        for i in range(len(intervals)):
            if endTime > intervals[i][0]:
                return False
            endTime = intervals[i][1]
        return True