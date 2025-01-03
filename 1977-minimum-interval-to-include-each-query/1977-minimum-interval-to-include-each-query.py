class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort() # O(nlogn)
        minHeap = [] # (length, right) to return shortest length
        res, i = {}, 0 # hashmap - map query to length

        # O(qlogq)
        for q in sorted(queries):
            # add element into minHeap
            while i<len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i+=1
            
            # pop invalid element in the minHeap
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1
            
        return [res[q] for q in queries]