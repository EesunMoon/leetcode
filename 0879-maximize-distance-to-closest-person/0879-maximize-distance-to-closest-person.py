class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # 1: person, 0: empty 7
        # 1 0 1 0 0 0 0 --> num(seats)-l(2)-1
        # 0 0 0 0 0 0 1 --> r-l
        #      0,1,0,0,1,0,1
        # prev.  p     n. 1, 4 n-p-1
        # 3 --> 2, 1 --> 1
        # 1,0,0,0,0,1: 4-->2
        # (zero-count+1)//2

        prev = -1
        res = 1
        for nxt in range(len(seats)):
            if seats[nxt] == 1:
                # beginning
                if prev == -1:
                    res = max(res, nxt)
                # boundary
                if prev != -1 and prev != nxt:
                    res = max(res, (nxt-prev)//2)
                prev = nxt
        # tailing
        if prev < len(seats)-1:
            res = max(res, len(seats)-prev-1)

        return res