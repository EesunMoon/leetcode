class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # n: len(s), m: len(queries)
        # BF O(m*n)

        # Closet Candle position
        # **|**|***|
        # prefix: -1 -1 2 2 2 5 5 5 5 9 # left boundary 
        # suffix:  2  2 2 5 5 5 9 9 9 9 # right boundary
        # candles: 0  0 1 1 1 2 2 2 2 3
        # => if candle: prefix == suffix
        # [2, 5] => prefix[2] = 2, prefix[5] = 5
        #        => suffix[2] = 2, suffix[5] = 5 
        # :: (length - 2(candle)) => (5-2+1)-2
        # [0, 6] => prefix[0] = -1, prefix[6] = 5
        #        => suffix[0] =  2, suffix[6] = 9
        #        => max(prefix[0], suffix[0]) ~ min(prefix[6], prefix[6])
        # [3, 8] => prefix[3] = 2, prefix[8] = 5
        #        => suffix[3] = 5, suffix[8] = 9

        # S O(n) or O(m), T O(n)
        n = len(s)
        prefix = [-1] * n # closet leftmost position
        suffix = [n] * n  # closet rightmost position
        candles = [0] * n
        # update prefix and suffix
        candle = -1
        totalCandle = 0
        for i in range(n):
            if s[i] == "|": 
                candle = i
                totalCandle += 1
            prefix[i] = candle
            candles[i] = totalCandle
        
        candle = n
        for i in range(n-1, -1, -1):
            if s[i] == "|": 
                candle = i
            suffix[i] = candle

        print(prefix)
        print(suffix)
        res = []
        for left, right in queries:
            if (left == right) or (totalCandle == 0):
                res.append(0)
                continue          

            preL, preR = prefix[left], prefix[right]
            sufL, sufR = suffix[left], suffix[right]

            left_boundary = max(preL, sufL)
            right_boundary = min(preR, sufR)
            numCandle = candles[right_boundary] - candles[left_boundary] - 1
            cnt = (right_boundary-left_boundary-1) - numCandle if (right_boundary-left_boundary-1) - numCandle >= 0 else 0
            res.append(cnt)

        return res

        