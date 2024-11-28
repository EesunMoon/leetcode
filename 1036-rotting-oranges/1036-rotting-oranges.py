class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # initialize
        rotten = []
        fresh, time = 0, 0
        visited = set() 
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
                    visited.add((r, c))
        
        if fresh == 0:
            return 0

        # BFS
        queue = deque(rotten)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while rotten:

            rotten = []
            while queue:
                r, c = deque.popleft(queue)
                for dr, dc in directions:
                    candr, candc = r + dr, c + dc
                    if candr not in (-1, ROWS) and candc not in (-1, COLS):
                        if (grid[candr][candc] == 1) and ((candr, candc) not in visited):
                            visited.add((candr, candc))
                            rotten.append((candr, candc))
                            fresh -= 1
            time += 1
            if fresh == 0:
                return time
            queue = deque(rotten)


        return time if fresh == 0 else -1