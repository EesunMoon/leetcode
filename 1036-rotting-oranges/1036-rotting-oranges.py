import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1. count fresh orange / add rotten in deque
        queue = collections.deque() # save rotten coordinate
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # fresh
                    fresh += 1
                elif grid[r][c] == 2: # rotten
                    queue.append((r, c)) 
        
        # base case
        if fresh == 0:
            return 0
        
        # 2. traversal BFS - count minutes , terminate if not queue
        time = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh != 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # track 4-directionally adjacent cell
                for dr, dc in directions:
                    candr, candc = dr + r, dc + c
                    
                    # invalid condition
                    if (candr < 0 or candr >= ROWS or candc < 0 or candc >= COLS or
                        grid[candr][candc] != 1):
                        continue
                    
                    # proceeding rotten
                    grid[candr][candc] = 2 # marked as visited (rotten)
                    fresh -= 1
                    queue.append((candr, candc))
            
            time += 1


        return time if fresh == 0 else -1