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