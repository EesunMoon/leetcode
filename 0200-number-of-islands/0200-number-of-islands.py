class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        M, N = len(grid), len(grid[0])
        res = 0
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0" # seen
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    candr, candc = dr+r, dc+c
                    if candr <0 or candc<0 or candr>=M or candc>=N or grid[candr][candc] =="0":
                        continue
                    q.append((candr, candc))
                    grid[candr][candc] = "0"

        for r in range(M):
            for c in range(N):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        
        return res