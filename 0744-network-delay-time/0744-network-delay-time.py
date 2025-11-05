class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # TC O(VlogE) SC O(V+E)
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append([v,w])
        
        minHeap = [(0,k)] #[w, v]
        minTime = 0 # return
        visited = set()
        while minHeap and len(visited) < n:
            currWeight, currNode = heapq.heappop(minHeap)
            if currNode in visited:
                continue
            
            minTime = currWeight
            visited.add(currNode)

            for neiNode, neiWeight in adj[currNode]:
                if neiNode not in visited:
                    heapq.heappush(minHeap, (currWeight+neiWeight, neiNode))

        return minTime if len(visited)==n else -1
