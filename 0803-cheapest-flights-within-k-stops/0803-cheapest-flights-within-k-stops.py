class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append([v,w])
        
        prices = [float("INF")] * n
        prices[src] = 0
        q = deque([(src, 0)]) # source and cost

        while q and k >= 0:
            k -= 1
            for _ in range(len(q)):
                node, cost = q.popleft()
                for neiNode, neiCost in adj[node]:
                    newCost = cost + neiCost
                    if newCost < prices[neiNode]:
                        prices[neiNode] = newCost
                        q.append((neiNode, prices[neiNode]))
        return prices[dst] if prices[dst]!=float("inf") else -1

        """
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
        """
