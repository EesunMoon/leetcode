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
        hashmap = {} # color: (index)
        ballmap = {} # index: color
        for x, y in queries:
            
            prev = ballmap.get(x, -1)
            if prev != -1:
                hashmap[prev].remove(x)
                if len(hashmap[prev]) == 0:
                    del hashmap[prev]
            
            ballmap[x] = y
            if not y in hashmap:
                hashmap[y] = set()
            hashmap[y].add(x)
            res.append(len(hashmap))
        
        return res

        