class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # [username[i], website[i], timestamp[i]]
        # username[i] -> website[i] in timestamp[i]
        # home -> away -> love 
        # home -> home -> home
        # home -> away -> home 
        # hashmap: key(username): value([website, timestamp])
        # Joe: [home, 1], [about, 2], [career, 3]
        # James: [home, 4], [cart, 5], [maps, 6], [home, 7]
        # Mary: [home. 8], [about, 9], [career, 10]

        # 1) sorted data based on timestamp
        data = sorted(zip(timestamp, username, website))

        # mapping username and website
        hashmap = defaultdict(list) # username: website
        for _, name, site in data:
            hashmap[name].append(site)
        
        patterns = defaultdict(int)
        for name, site in hashmap.items():
            seen = set()
            for i in range(len(site)-2):
                for j in range(i+1, len(site)-1):
                    for k in range(j+1, len(site)):
                        cand = tuple([site[i], site[j], site[k]])
                        if cand not in seen:
                            seen.add(cand)
                            patterns[cand] += 1
        
        return sorted(patterns.keys(), key=lambda x: (-patterns[x], x))[0]
        