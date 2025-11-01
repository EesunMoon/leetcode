class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        # starting from 0: dist 0
        # add not zero (adjacent to the 0) --> dist 1
        q = deque()
        seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c,0)) # r, c, dist
                    seen.add((r,c))
        directions = [(0,1),(0,-1), (1,0), (-1,0)]
        while q:
            r, c, dist = q.popleft()
            mat[r][c] = dist
            for dr, dc in directions:
                cr, cc = dr+r, dc+c
                if (cr<0 or cr>=ROWS or cc<0 or cc>=COLS or (cr,cc) in seen):
                    continue
                q.append((cr,cc,dist+1))
                seen.add((cr,cc))
        return mat
