class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashmap = {}
        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)
        
        H = [[-cnt, c] for c, cnt in hashmap.items()]
        heapq.heapify(H)

        prev = None
        ans = ""
        while H or prev:
            # impossible case
            if prev and not H:
                return ""
            
            cnt, c = heapq.heappop(H)

            cnt += 1
            ans += c

            if prev:
                heapq.heappush(H, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, c]

        return ans
        