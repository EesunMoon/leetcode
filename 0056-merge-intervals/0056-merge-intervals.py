class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # O(nlogn)
        for start, end in sorted(intervals):
            if not res:
                res.append([start, end])
                continue

            priorStart, priorEnd = res[-1][0], res[-1][1]
            # overlap
            if priorEnd >= start:
                res[-1][0], res[-1][1] = min(priorStart, start), max(priorEnd, end)
            else:
                res.append([start, end])
            
        return res