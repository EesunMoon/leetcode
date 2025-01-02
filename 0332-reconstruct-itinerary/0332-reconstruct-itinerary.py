class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = defaultdict(list) # adj list
        # tickets.sort() # lexical order
        for src, dst in sorted(tickets)[::-1]: # sorted reverse order
            adj[src].append(dst)
        
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs("JFK")
        return res[::-1]