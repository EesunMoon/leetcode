import math
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        EMPTY = float("inf")
        GATE = 0
        WALL = -1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        m = len(rooms)

        if m == 0:
            return
        n = len(rooms[0])
        queue = deque()

        # save GATE info(row, col)
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == GATE:
                    queue.append((row, col))
        print(queue)
        while queue:
            # start with GATE
            row, col = queue.popleft()

            candidate_distance = rooms[row][col] + 1
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r in (-1, m) or c in (-1, n) or (rooms[r][c]== WALL):
                    continue
                if candidate_distance < rooms[r][c]:
                    # Fine distance by searching room of distance + 1
                    rooms[r][c] = candidate_distance
                    queue.append((r,c))
        