class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        Limit 4 -> 0, 1, 2, 3, 4 :: the number of balls - 5 (limit + 1)
        query [x , y] -> x, y represent the labels of balls
            x <- y

               0 1 2 3 4    
        [1, 4] 0 4 0 0 0 -> 1
        [2, 5] 0 4 5 0 0 -> 2
        [1, 3] 0 3 5 0 0 -> 2
        [3, 4] 0 3 5 4 0 -> 3

        hashmap: color:[index]
        """
        # TC O(m), O(n)
        res = [] # contain the results for each query
        colormap = {} # color: freq
        ballmap = {} # index: color
        for x, y in queries:
            
            prev = ballmap.get(x, -1) # previous ball's color
            if prev != -1:
                colormap[prev] -= 1
                if colormap[prev] == 0:
                    del colormap[prev]
            
            ballmap[x] = y
            colormap[y] = 1 + colormap.get(y, 0)
            res.append(len(colormap))
        
        return res

        