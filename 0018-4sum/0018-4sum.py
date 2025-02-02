class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # binary search

        nums.sort() # O(nlogn)

        # O(n**3)
        res = []
        for i in range(len(nums)-3):
            # prevent duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]
            for j in range(i+1, len(nums)-2):
                # prevent duplicates
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                num2 = nums[j]

                l, r = j+1, len(nums)-1
                while l<r:
                    cand = num1 + num2 + nums[l] + nums[r]
                    if cand > target:
                        r -= 1
                    elif cand < target:
                        l += 1
                    else:
                        res.append([num1, num2, nums[l], nums[r]])
                        l += 1
                        # prevent duplicates
                        while l<r and nums[l] == nums[l-1]:
                            l += 1
        return res

