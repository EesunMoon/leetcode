class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash table
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        print(points)
        print(max_number)

        cache = {}
        def dp(idx):
            # base case
            if idx == 0:
                return 0
            if idx == 1:
                return points[1]
            
            if idx not in cache:
                cache[idx] = max(points[idx]+dp(idx-2), dp(idx-1))
            return cache[idx]
        
        return dp(max_number)