# from collections import Counter
from bisect import bisect_left

class Solution(object):
    def minOperations(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        prefix = [0] * (len(nums)+1)
        
        # cumulative sum
        for i in range(len(nums)):
            prefix[i+1] += prefix[i] + nums[i]
        print(prefix)

        answer = []
        for query in queries:
            idx = bisect_left(nums, query) # find index where query in nums
            print(idx)
            left = idx * query - prefix[idx]
            right = (prefix[-1] - prefix[idx]) - (len(nums) - idx) * query
            answer.append(left+right)

        
        return answer
                

        """
        ## HashTable - Time limited

        nums_dict = Counter(nums)
        result = []
        # print(nums_dict)
        # print(nums_dict.items())
        
        for query in queries:
            total = sum([abs(k-query)*v for k,v in nums_dict.items()])
            result.append(total)

        return result
        """
        