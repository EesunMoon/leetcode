class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        res = []
        for i in range(len(intervals)):
            currStart, currEnd = intervals[i]
            if newStart > currEnd: # X overlap
                res.append([currStart, currEnd])
            elif newEnd < currStart: # O overlap + curr X overlap
                res.append([newStart, newEnd])
                return res + intervals[i:]
            else: # O overlap
                newStart, newEnd = min(currStart, newStart), max(newEnd, currEnd)
        res.append([newStart, newEnd]) # last case
        return res
