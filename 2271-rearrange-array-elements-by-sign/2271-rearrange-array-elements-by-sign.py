class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # constraint: 
        # 1. len(nums) % 2 == 0
        # 2. len(positive) == len(negative)
        # condition: 
        # 1. start positivie num
        # 2. rearrange: pos, neg, pos, neg

        # two pointer TC O(n) SC O(1)
    
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
        