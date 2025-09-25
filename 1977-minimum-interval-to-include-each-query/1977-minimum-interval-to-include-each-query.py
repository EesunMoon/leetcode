class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sizes = [] # minheap [size, right]
        intervals.sort()
        idx = 0 # intervals index
        mapping = {} # query: size

        for q in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= q:
                l, r = intervals[idx]
                heapq.heappush(sizes, [r-l+1, r])
                idx += 1
            
            while sizes and sizes[0][1] < q:
                heapq.heappop(sizes)
            mapping[q] = sizes[0][0] if sizes else -1

        return [ mapping[q] for q in queries]
