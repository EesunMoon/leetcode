class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1. 0: empty, 1: fresh, 2: rotten
        # 2. rotten spreads 4 direction -> BFS
        # return: minimum number of minutes (all oranges are rotten), imposs->-1
        # edge case) if there're no rotten --> -1
        #                       no fresh --> 0
        #            fresh is seperate from any rotten --> -1

        # bfs:
        # 1. collect original rotten oranges + count how many fresh oranges are there
        # 2. collect adjancent fresh orange to (1) rotten oranges 

        fresh = 0
        q = deque()
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # fresh
                    fresh += 1
                elif grid[r][c] == 2: # rotten
                    q.append((r, c))
                    grid[r][c] = 0 # visited
        if fresh == 0: # no fresh
            return 0
        if not q: # no rotten
            return -1

        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        while q and fresh > 0:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.popleft()
                for dr, dc in directions:
                    cr, cc = dr+r, dc+c
                    if (cr < 0 or cr >=ROWS or cc <0 or cc>=COLS or grid[cr][cc] == 0):
                        continue # invalid or already visited or empty
                    q.append((cr,cc))
                    grid[cr][cc] = 0 # visited
                    fresh -= 1
            res += 1

        return res if fresh == 0 else -1