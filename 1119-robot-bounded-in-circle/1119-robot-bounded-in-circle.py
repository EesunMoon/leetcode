class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
            north: x, y + 1 (0)
            south: x, y - 1 (2)
            east: x+1, y    (1)
            west: x-1, y    (3)
        """
        direction = 0
        
        x, y = 0, 0
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for s in instructions:    
            if s == "G":
                x += move[direction][0] 
                y += move[direction][1]
            elif s == "L":
                direction = (4 + direction - 1) % 4
            elif s == "R":
                direction = (4 + direction + 1) % 4
        
        return (x == 0 and y == 0) or direction != 0