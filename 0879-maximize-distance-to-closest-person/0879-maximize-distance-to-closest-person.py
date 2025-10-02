class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        prev = -1
        ans = 0

        for i, v in enumerate(seats):
            if v == 1:
                if prev == -1:
                    ans = max(ans, i)
                else:
                    gap = i - prev - 1
                    ans = max(ans, (gap+1)//2)
                prev = i
        if prev != -1:
            ans = max(ans, n-prev-1)
        return ans