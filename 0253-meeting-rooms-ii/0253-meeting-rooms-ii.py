class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        endlist = []
        for start, end in intervals:
            if endlist and endlist[0] <= start:
                heapq.heappop(endlist)
            heapq.heappush(endlist, end)

        return len(endlist)