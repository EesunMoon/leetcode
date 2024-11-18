class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        if len(sticks) == 1:
            return 0
        
        heapq.heapify(sticks)
        costs = 0
        
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            cost = first+second
            costs+=cost
            heapq.heappush(sticks, cost)

        return costs