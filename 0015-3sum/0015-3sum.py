class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # O(nlogn) to perform binary search

        for k in range(len(nums)-2):
            # prevent duplicates
            if k > 0 and nums[k] == nums[k-1]:
                continue

            # perform binary search
            target = nums[k]
            l, r = k+1, len(nums)-1
            while l<r:
                cand = target + nums[l] + nums[r]

                if cand > 0:
                    r -= 1
                elif cand < 0:
                    l += 1
                else:
                    res.append([target, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
            