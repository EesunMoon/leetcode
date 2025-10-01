class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = "0" # mark as visited

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    candr, candc = r+dr, c+dc
                    if ((0<=candc<COLS) and (0<=candr<ROWS) and (grid[candr][candc] == "1")):
                        q.append((candr, candc))
                        grid[candr][candc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1

        return res