class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, seen, prevHeight):
            if r in (-1, ROWS) or c in (-1, COLS) or (r, c) in seen or heights[r][c] < prevHeight:
                return

            seen.add((r, c))
            dfs(r+1, c, seen, heights[r][c])
            dfs(r-1, c, seen, heights[r][c])
            dfs(r, c+1, seen, heights[r][c])
            dfs(r, c-1, seen, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
                

