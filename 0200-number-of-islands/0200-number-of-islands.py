class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        num_islands = 0
        self.m, self.n = len(grid), len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    grid[i][j] = "0" # mark as visited
                    num_islands += 1
                    queue = deque()
                    queue.append((i,j))
                    while queue:
                        row, col = queue.popleft()
                        if row-1 >=0 and grid[row-1][col] == "1":
                            queue.append((row-1, col))
                            grid[row-1][col] = "0"
                        if row+1 < self.m and grid[row+1][col] == "1":
                            queue.append((row+1, col))
                            grid[row+1][col]="0"
                        if col-1 >=0 and grid[row][col-1] == "1":
                            queue.append((row, col-1))
                            grid[row][col-1] ="0"
                        if col+1 < self.n and grid[row][col+1] == "1":
                            queue.append((row, col+1))
                            grid[row][col+1]="0"

        return num_islands