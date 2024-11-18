class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        
        ladder_possible = []

        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]

            if climb <= 0:
                continue
            
            # use ladders for the longest climbs
            heapq.heappush(ladder_possible, climb)
            if len(ladder_possible) <= ladders:
                continue
            
            # use bricks for the shortest climbs => min_heap
            bricks -= heapq.heappop(ladder_possible)
            if bricks < 0:
                return i

        # covered every climb 
        return len(heights) - 1