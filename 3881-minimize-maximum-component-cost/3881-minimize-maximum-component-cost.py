class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if n <= k:
            return 0
        
        res = float("inf")
        l, r = 0, 0
        for _, _, w in edges:
            r = max(r, w)

        def bfs(thres):
            adj = collections.defaultdict(list)
            # only include the edge's weight is lower than thres
            for u, v, w in edges:
                if w <= thres:
                    adj[u].append([v,w])
                    adj[v].append([u,w])

            cnt, maxC = 0, 0
            q = collections.deque()
            visited = set()
            for node in range(n):
                if node in visited:
                    continue
                q.append(node)
                visited.add(node)
                while q:
                    curr = q.popleft()
                    if curr not in adj:
                        continue
                    for nei, w in adj[curr]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                            maxC = max(maxC, w)
                cnt += 1
            return cnt, maxC
                    
        while l<=r:
            m = (l+r)//2
            cnt, maxC = bfs(m)
            if cnt > k: # threshold is too small
                l = m+1
            else: # threshold is too big
                res = min(res, maxC)
                r = m-1
            
        return res
            