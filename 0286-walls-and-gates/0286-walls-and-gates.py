import math
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        queue = deque()
        visited = set() # prevent from tracking visited node again

        for r in range(ROWS):
            for c in range(COLS):
                # start from gate
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = dist

                for dr, dc in directions:
                    candr, candc = dr + r, dc + c

                    if candr in (-1, ROWS) or candc in (-1, COLS) or rooms[candr][candc] == -1 or (candr, candc) in visited:
                        continue
                    queue.append((candr, candc))
                    visited.add((candr, candc))
            dist += 1




        