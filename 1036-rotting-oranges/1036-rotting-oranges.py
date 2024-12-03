class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh = 0
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        res = 1

        # initialize
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    grid[r][c] = 0 # mark as visited
        
        if fresh == 0:
            return 0
        
        # track
        while queue:
            # level
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    candr, candc = dr+r, dc+c
                    if (candr in (-1, ROWS) or candc in (-1, COLS) 
                        or grid[candr][candc] == 0):
                        continue
                    queue.append((candr, candc))
                    grid[candr][candc] = 0 # mark as visited
                    fresh -= 1
            # print(queue, res)
            if fresh == 0:
                break
            res += 1                        

        return res if fresh == 0 else -1