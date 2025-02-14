class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # constraint: 
        # 1. len(nums) % 2 == 0
        # 2. len(positive) == len(negative)
        # condition: 
        # 1. start positivie num
        # 2. rearrange: pos, neg, pos, neg

        # two pointer TC O(n) SC O(1)
        pos, neg = 0, 1
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2
        return ans


        """
        # High-level TC O(n) SC O(n)
        if len(nums) == 0:
            return []

        pos = []
        neg = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res
        """