class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        
        # O(logm)
        def getDigit(num):
            res = 0
            while num:
                res += (num%10)
                num //= 10
            return res
        

        # digitsum: [num] -> TC O(nlogm) SC O(logm)
        digitMap = defaultdict(list)
        for num in nums:
            digit = getDigit(num) # O(logm)
            heapq.heappush(digitMap[digit], num)
            if len(digitMap[digit]) > 2: # O(1)
                heapq.heappop(digitMap[digit])

        res = 0
        for group in digitMap.values():
            if len(group) == 2:
                n1 = heapq.heappop(group)
                n2 = heapq.heappop(group)
                res = max(res, n1+n2)
        return res if res != 0 else -1