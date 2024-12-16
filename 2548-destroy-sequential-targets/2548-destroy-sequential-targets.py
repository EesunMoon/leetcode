class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        hashmap = {} # (mod(%):(cnt, minumum target(seed) val))
        mx = 0

        for num in nums:
            x = num%space # mod(%) - target

            if x not in hashmap:
                hashmap[x] = (1, num)
            else:
                hashmap[x] = (hashmap[x][0]+1, min(hashmap[x][1], num))
            
            mx = max(mx, hashmap[x][0])
        

        mi = float("inf")
        for x in hashmap.values():
            if mx == x[0]:
                mi = min(mi, x[1])

        return mi