class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        # sliding window: T O(n) S O(1)
        l = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
                continue
            res = max(res, prices[r] - prices[l])

        return res