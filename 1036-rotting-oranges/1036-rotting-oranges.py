class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # initialization
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        # edge case
        if fresh == 0:
            return 0

        # bfs
        res = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    candr, candc = dr + r, dc + c
                    if candr in (-1, ROWS) or candc in (-1, COLS) or grid[candr][candc] != 1:
                        continue
                    queue.append((candr, candc))
                    fresh -= 1
                    grid[candr][candc] = 2
            res += 1

        return res if fresh == 0 else -1
