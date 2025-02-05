class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix & hashmap
        """
            prefix[i] = sum(0~i), prefix[j] = sum(0~j)
            sum(i~j) = sum(0 ~ j) - sum(0 ~ i-1) = k (i<j)
                => sum(0~j) - k = sum(0~i-1)
                => prefix[j] - k = prefix[i-1]
                => if current prefix - k is in hashmap(that store the prior prefix?)
            hashmap: (subSum: freq)
                base case) 0: 1
        """
        count = {0:1} # subSum: freq
        prefix = 0
        res = 0
        for num in nums:
            prefix += num # current (prefix[j])
            res += count.get(prefix-k, 0)
            
            count[prefix] = 1 + count.get(prefix, 0) # store (current become prior num in next)
        return res
        
        # brute force algorithm TC O(n^2) SC O(1)
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total == k:
                    cnt += 1
                    break
        return cnt
        """