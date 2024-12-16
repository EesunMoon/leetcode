class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        hashmap = {} # mod: (maximum cnt, minimum value)
        mx = 0

        for num in nums:
            x = num % space
            if x not in hashmap:
                hashmap[x] = (1, num)
            else:
                hashmap[x] = (hashmap[x][0]+1, min(hashmap[x][1], num))
            
            mx = max(mx, hashmap[x][0])
        
        res = float('inf')
        for val in hashmap.values():
            if val[0] == mx:
                res = min(res, val[1])
        
        return res
        