class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
            count = 0, cand = None
            track the nums
            if count == 0: cand = num
            count += 1 if cand == num else -1
        """
        cnt = 0
        cand = None
        for n in nums:
            if cnt == 0:
                cand = n
            cnt += 1 if cand == n else -1
        return cand
        
        # sorting
        nums.sort()
        return nums[len(nums)//2]