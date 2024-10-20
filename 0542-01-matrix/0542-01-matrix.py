from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        # initialization
        matrix = [row[:] for row in mat] # copy - weight matrix
        m = len(matrix) # row
        n = len(matrix[0]) # column
        queue = deque()
        seen = set()
        
        # queue: if weight is 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0)) # index_x, index_y, weight
                    seen.add((row, col)) # index
        
        directions = [(0, 1), (1,0), (0,-1), (-1,0)] # matrix direction
        
        # BFS
        while queue:
            row, col, steps = queue.popleft()
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                
                # if weight is not 0
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps+1))
                    matrix[next_row][next_col] = steps+1
                    
        return matrix
        