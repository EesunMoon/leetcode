class Solution:
    def frequencySort(self, s: str) -> str:
        # TC O(nlogn) SC O(n)
        if not s:
            return ""
        
        hashmap = {} # char: freq

        # 1) counting the freq
        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)

        # 1-2) create bucket: index=freq, element=char
        max_freq = max(hashmap.values())
        bucket = [[] for _ in range(max_freq+1)]
        for c, freq in hashmap.items():
            bucket[freq].append(c)
        
        # return
        res = ""
        for freq in range(len(bucket)-1, 0, -1):
            for c in bucket[freq]:
                res += (c*freq)
        return res


        """
        # 2) sort hashmap in decreasing freq order
        hashmap = sorted(hashmap.items(), key=lambda x:-x[1])
        
        # 3) return
        res = ""
        for c, freq in hashmap:
            res += (c*freq)
        return res
        """