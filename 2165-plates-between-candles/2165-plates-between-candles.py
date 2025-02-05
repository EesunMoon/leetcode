class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
            k: len(queires), n: len(s)
            brute force: TC O(k*n) SC O(1)
            
            candles: 0,  0, 1, 1, 1, 2, 2, 2, 2, 3
            before: -1, -1, 2, 2, 2, 5, 5, 5, 5, 9 
            after:   2,  2, 2, 5, 5, 5, 9, 9, 9, 9
                -> if candle: before == after
                    [2, 5] 2, 5 :: (5-2)-1
                    [1, 6] max(-1, 2), min(5, 9) 2, 5 :: (5-2)-1
                    [3, 7] max(2, 5), min(5, 9) 5, 5:: (5-5)-1 < -1
                    []
            1) store candle index in before, after array:: TC O(n), SC O(n)
            2) compute the number of plates between candle for each query:: TC O(k)
            =>> TC O(n+k), SC O(n)
        """
        n = len(s)
        # 1) store candle index information 
        # 1-1) fill before array as well as prefix candle num
        before = [-1] * (n)
        candles = [0] * n
        candle, cnt = -1, 0
        for i in range(n):
            if s[i] == "|":
                candle = i
                cnt += 1
            before[i] = candle
            candles[i] = cnt

        # 1-2) fill after array
        after = [n] * (n)
        candle = n
        for i in range(n-1, -1, -1):
            if s[i] == "|":
                candle = i
            after[i] = candle
        
        # 2) compute the number of plates between candle for each query:: TC O(k)
        res = []
        for l, r in queries:
            # base case
            if l >= r or cnt == 0:
                res.append(0)
                continue
            left, right = max(before[l], after[l]), min(before[r], after[r])
            candleNum = candles[right] - candles[left] - 1
            num = (right - left - 1) - candleNum if (right - left - 1) - candleNum > 0 else 0
            res.append(num)
        return res