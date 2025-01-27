class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def search(r, c):
            """
            # DFS O(n*m)
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0" # mark as visited

            for dr, dc in directions:
                search(dr+r, dc+c)
            """
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0" # marked as visited

            # BFS O(n*m)
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        candr, candc = dr + r, dc + c
                        if (candr < 0 or candr >= ROWS or candc < 0 or candc >= COLS 
                            or grid[candr][candc] == "0"):
                            continue

                        queue.append((candr, candc))
                        grid[candr][candc] = "0"

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    search(r, c)
                    res += 1
        return res