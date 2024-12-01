class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        cnt = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0" # visited mark

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    candr, candc = dr + r, dc + c
                    if (candr not in (-1, ROWS) and candc not in (-1, COLS)):
                        if grid[candr][candc]== "1":
                            queue.append((candr, candc))
                            grid[candr][candc] = "0" # visited mark


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    cnt += 1
        
        return cnt