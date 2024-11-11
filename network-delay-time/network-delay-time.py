class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0,k)]
        seen = set()
        max_cost = 0

        while heap:
            cost, node = heapq.heappop(heap)
            if node in seen:
                continue
            
            seen.add(node)
            max_cost = max(max_cost, cost)
            
            for cand_node, cand_cost in graph[node]:
                if cand_node not in seen:
                    curr_cost = cost + cand_cost
                    heapq.heappush(heap, (curr_cost, cand_node))
        
        return max_cost if len(seen) == n else -1