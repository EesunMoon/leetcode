class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("INF")] * n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()

            for s, d, p in flights: # source, destination, prices
                if prices[s] == float("INF"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s]+p
            prices = tmpPrices
        return prices[dst] if prices[dst] != float("INF") else -1
