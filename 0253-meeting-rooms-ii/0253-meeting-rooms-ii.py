class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        rooms = [0]

        # sort by start time in increasing order
        heapq.heapify(intervals)

        while intervals:
            start, end = heapq.heappop(intervals)

            rooms.sort()
            flag = False
            for i in range(len(rooms)):
                if rooms[i] <= start:
                    rooms[i] = end
                    flag = True
                    break

            if not flag:
                rooms.append(end)
            
        # print(rooms)
        return len(rooms)