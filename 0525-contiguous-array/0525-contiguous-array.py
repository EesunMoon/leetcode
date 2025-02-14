class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # brute force: O(n**2)
        # prefix_sum: consider 0 as -1 <<- if num.1 and n.0 is same, 0
        # [0, 0, 1,  0, 0,0, 1, 1]
        # [-1,-2,-1,-2,-3,-4,-3,-2]
        # [0, 1, 0, 1]
        # [-1,0,-1, 0]
        # 0: idx
        prefix_sum = 0
        sum_idx = {0:-1} # subSum: index
        res = 0
        
        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1
            if prefix_sum == 0:
                res = i + 1
            elif prefix_sum in sum_idx:
                res = max(res, i - sum_idx[prefix_sum])
            else:
                sum_idx[prefix_sum] = i
        return res