class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort() # O(nlogn)
        for k in range(len(nums)):
            target = nums[k]

            # prevent duplicate
            if k != 0 and nums[k] == nums[k-1]:
                continue
            
            # binary search
            i, j = k + 1, len(nums)-1
            while i < j:
                cand = target + nums[i] + nums[j]

                if cand < 0:
                    i += 1
                elif cand > 0:
                    j -= 1
                else:
                    res.append([target, nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
        return res