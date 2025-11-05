class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("INF")] * n
        prices[src] = 0

        for i in range(k+1): # stop
            tmpPrices = prices.copy()

            for s, d, cost in flights:
                if prices[s] == float("INF"):
                    continue
                
                if prices[s] + cost < tmpPrices[d]: # current prices + reached prices
                    tmpPrices[d] = prices[s] + cost
            prices = tmpPrices
        return prices[dst] if prices[dst] != float("INF") else -1

