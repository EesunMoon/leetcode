class Solution:
    def reorganizeString(self, s: str) -> str:
        # make hashmap : T O(n) S O(k)
        count = {}
        for st in s:
            count[st] = 1 + count.get(st, 0)
        
        H = [] # build max heap T O(klogk) S O(k)
        for st, freq in count.items():
            heapq.heappush(H, (-freq, st))
        
        # O(nlogk)
        prev = None
        res = ""
        while H:
            freq, st = heapq.heappop(H)
            res += st
            freq += 1 # to make zero

            if prev:
                heapq.heappush(H, prev)
            if freq != 0:
                prev = (freq, st)
            else:
                prev = None
            
        return res if len(res) == len(s) else ""