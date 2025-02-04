class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # ladder: use the maximum jump as possible
        # firstly, use bricks as long as bricks are avaialbe ( bricks != 0 )
        # store differ in max heap of bricks
        # if bricks are not available => in maximum value in max heap :: ladder if possible
        # if ladder are available -> add the value of max heap to bricks again (since we use ladder)
        # otherwise, return !

        max_heap = [] # store difference in order decreasing order

        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]

            if diff <= 0:
                continue

            # use bricks first
            heapq.heappush(max_heap, -diff) # to make max heap
            bricks -= diff
            if bricks < 0:
                if ladders == 0:
                    return i # since we cannot go to next building
                ladders -= 1
                bricks += (-heapq.heappop(max_heap))
        return len(heights)-1 # if all building