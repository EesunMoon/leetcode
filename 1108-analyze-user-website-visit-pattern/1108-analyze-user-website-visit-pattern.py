class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        1. sorted by timestamp
        2. group by username using hashmap ex) username: [pattern]
        3. get pattern map by iterating each usergroup pattern combination (pattern length 3) 
            ex) pattern: freq
            => prevent duplicates in same group
        4. return maximum score of pattern by sorting in decreasing order of 
        """
        
        # 1. sorted by timestamp: TC O(nlogn) SC O(n)
        data = sorted(zip(timestamp, username, website))

        # 2. group by username using hashmap (ex) username: [pattern]: TC O(n) SC O(n/3)
        usermap = defaultdict(list)
        for _, name, site in data:
            usermap[name].append(site)
        
        # 3. get patternmap by iterating each usermap TC O(n^3) SC O(k)
        patternmap = defaultdict(int)
        for name, patterns in usermap.items():
            seen = set() # prevent duplicates
            for i in range(len(patterns)-2):
                for j in range(i+1, len(patterns)-1):
                    for k in range(j+1, len(patterns)):
                        cand = tuple([patterns[i], patterns[j], patterns[k]])
                        if cand not in seen:
                            patternmap[cand] += 1
                            seen.add(cand)
        
        # 4. return maximum score of pattern
        return sorted(patternmap.keys(), key=lambda x:(-patternmap[x], x))[0]
        