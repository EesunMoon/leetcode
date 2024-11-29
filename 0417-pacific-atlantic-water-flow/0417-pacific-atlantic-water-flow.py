class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # visted

        def dfs(r, c, visited, prevHeights):
            if ((r, c) in visited or 
                r in (-1, ROWS) or c in (-1, COLS)
                or heights[r][c] < prevHeights):
                return
            visited.add((r,c))

            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # pac
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) # atl
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # pac
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # atl
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
