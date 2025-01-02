class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # approach 2) Bellman Ford - DP
        prices = [float("INF")] * n
        prices[src] = 0

        # consider k-th stop
        for _ in range(k+1):
            tmpPrices = prices[:] # .copy()

            for s, d, p in flights:
                if prices[s] == float("INF"):
                    continue
                # update
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return prices[dst] if prices[dst]!=float("INF") else -1 
     
        
        """
        # approach 1) Dijistra
        graph = defaultdict(list)
        for start, end, weight in flights:
            graph[start].append((end, weight))
        
        queue = [(0, 0, src)] # (cost, k, src)
        visited = {}

        while queue:
            weight, cnt, start = heapq.heappop(queue)
            if start == dst and cnt-1 <= k:
                return weight
            if start not in visited or visited[start] > cnt:
                visited[start] = cnt
                for new_end, new_weight in graph[start]:
                    heapq.heappush(queue, (weight+new_weight, cnt+1, new_end))
        
        return -1
        """