class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # greedy O(n) vs DP O(n^2)
        # sliding window + BFS

        l, r = 0, 0
        step = 0
        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            l, r = r, farthest
            step += 1
        return step