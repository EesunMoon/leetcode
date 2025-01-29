class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        cnt = 0
        freq = {0:1}
        """
        sum(i, j) = prefix[j] - prefix[i-1]
                k = prefix[j] - prefix[i-1]
                    prefix[i-1] = prefix[j] - k
        """

        for num in nums:
            prefix += num # prefix[j]
            if prefix - k in freq:
                cnt += freq[prefix-k]
            
            freq[prefix] = 1 + freq.get(prefix, 0) # next step: become prefix[i-1]
        return cnt
