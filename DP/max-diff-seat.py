class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        res = 0 # maximum distance
        last_person = -1
        
        for i in range(n):
            if seats[i] == 1:
                if last_person == -1:
                    res = i
                else:
                    res = max(res, (i - last_person) // 2)
                last_person = i
        
        res = max(res, n - 1 - last_person)
        return res
