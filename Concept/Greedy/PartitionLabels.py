class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # make hashmap T O(n*m) S O(m)
        """
        hashmap = {}
        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)
        
        res = []
        l = 0
        subSet = set()
        for r in range(len(s)):            
            subSet.add(s[r])
            hashmap[s[r]] -= 1
            
            # check all hashmap of elements in subelement are zero
            if hashmap[s[r]] == 0:
                flag = True
                for sub in subSet:
                    if hashmap[sub] != 0:
                        flag = False
                        break
                if flag:
                    res.append(r-l+1)
                    l = r + 1
        return res
        """
        # greedy + hashmap
        # save last occurence
        last = {c: i for i, c in enumerate(s)}
        res = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last[c]) # store max index among possible element(subSet)
            if i == end:
                res.append(end-start + 1)
                start = i + 1 # move next
        return res
                
