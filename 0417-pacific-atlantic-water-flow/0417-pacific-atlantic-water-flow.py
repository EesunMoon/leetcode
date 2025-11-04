class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        BF: every cell - DFS/BFS for pacific & atlantic 
            current cell height >= neighbor's cell height
            TC O(2(N*M)^2)
        Optimal: starting from pacific & atlantic - DFS/BFS 
            to check where ocean cell can reach
            duplicates --> result
            current cell height <= neighbor's cell height
            TC O(N*M)
        """
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        # pacific bound: row = 0 OR col = 0
        # atlantic bound: row = m-1 OR col = n-1

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or r<0 or r>=m or c<0 or c>=n
                or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r-1,c, visit, heights[r][c])
            dfs(r+1,c, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])

        for c in range(n):
            dfs(0, c, pacific, heights[0][c]) # pacific - first row
            dfs(m-1, c, atlantic, heights[m-1][c]) # pacific - last row
        for r in range(m):
            dfs(r,0, pacific, heights[r][0]) # pacific - first column
            dfs(r, n-1, atlantic, heights[r][n-1]) # pacific - last column
        
        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res