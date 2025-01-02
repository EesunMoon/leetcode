class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # approach: topological sort

        # define adjacent list
        adj = { c: set() for w in words for c in w }
        indegree = { c: 0 for c in adj }

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        # perform topological sort
        q = deque([ c for c in indegree if indegree[c] == 0 ])
        res = []

        while q:
            ch = q.popleft()
            res.append(ch)

            for nei in adj[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return "".join(res) if len(indegree) == len(res) else ""