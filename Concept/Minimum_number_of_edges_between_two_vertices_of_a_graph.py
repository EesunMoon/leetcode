"""
    For given graph G, find minimum number of edges between (1,5)
    edges = [[0, 1], [0, 2], [1, 2], [0, 4], 
            [3, 4], [4, 5], [4, 6], [2, 5]]
    vertices = 7
"""

import collections
import queue
def solution(edges, u, v, n):

    # init: O(E)
    adj = collections.defaultdict(list)
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    distance = 0
    Q = queue.deque([u])
    seen = set()
    seen.add(u)

    while Q:
        for _ in range(len(Q)):
            node = Q.popleft()

            for nei in adj[node]:
                if nei == v:
                    return distance + 1
                if nei in seen:
                    continue
                Q.append(nei)
                seen.add(nei)

        distance += 1
        # print(seen)
        # print(Q, distance)

    return -1


edges = [[0, 1], [0, 2], [1, 2], [0, 4], 
        [3, 4], [4, 5], [4, 6], [2, 5]]
n = 7
u, v = 3,2
print(solution(edges, u, v, n))

