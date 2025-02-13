class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
        
        hashmap = {} # char: freq

        # 1) counting the freq
        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)
        
        # 2) sort hashmap in decreasing freq order
        hashmap = sorted(hashmap.items(), key=lambda x:-x[1])
        
        # 3) return
        res = ""
        for c, freq in hashmap:
            res += (c*freq)
        return res