class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        original = heights[:]
        heapq.heapify(heights)
        expected = []
        
        while heights:
            min_val = heapq.heappop(heights)
            heapq.heapify(heights)
            expected.append(min_val)

        cnt = 0
        for o, e in zip(original, expected):
            if o != e:
                cnt +=1
        
        return cnt