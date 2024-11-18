class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        rooms = [] # priority queue

        # sort by start time in increasing order
        intervals.sort(key=lambda x: x[0])

        heapq.heappush(rooms, intervals[0][1]) # store end time

        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
            
        
        return len(rooms)