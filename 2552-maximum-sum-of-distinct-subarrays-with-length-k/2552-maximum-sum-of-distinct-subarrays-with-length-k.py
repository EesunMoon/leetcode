class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        constraint: len(nums) >= k >= 1
        
        sliding window
        1. distinct - hashSet
        2. Max subSum - prefix
            [1, 5,4, 2, 9, 9, 9]
            [1,6,10,12,21,30,39]
        """
        
        subSet = set()
        curr = 0
        res = 0 # max Sum
        
        l = 0
        for r in range(len(nums)):
            if nums[r] not in subSet:
                curr += nums[r]
                subSet.add(nums[r])
                if r-l+1 == k:
                    res = max(res, curr)
                    
                    # shrink window
                    curr -= nums[l]
                    subSet.remove(nums[l])
                    l += 1
            else:
                # shrink window
                while nums[l] != nums[r]:
                    curr -= nums[l]
                    subSet.remove(nums[l])
                    l += 1
                l += 1
        return res
                        



        # brute force: TC O((n-k)*k)
        """
        res = 0
        for i in range(len(nums)-k+1):
            subArray = nums[i:i+k]
            if len(set(subArray)) == k:
                res = max(res, sum(subArray))
        return res
        """