class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [0, 10], [10, 15] => [0, 15]
        """
            1) consider earlier starting interval
            2) consider shortest time
        """
        # [0, 17], [2, 8], [11, 13], [15, 20], [19, 21]
        # [0, 17], [2, 21] | [0, 21], [2, 13]
        # prior end time <= next start time:: can sum

        # TC O(nlogn) SC O(n)
        # Sorting in earlier starting time
        intervals.sort(key=lambda x:x[0]) # sorting O(nlogn)
        
        H = [] # track the earliest ending time
        heapq.heappush(H, intervals[0][1])

        for i in range(1, len(intervals)):
            # prior end time <= next start time
            if H[0] <= intervals[i][0]:
                heapq.heappop(H)
            heapq.heappush(H, intervals[i][1])
        return len(H)