class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = []
        def backtracking(i):
            if i == len(nums):
                res.append(subSet[:])
                return

            # contain current number
            subSet.append(nums[i])
            backtracking(i+1)

            # not contain current number
            subSet.pop()
            backtracking(i+1)

        backtracking(0)
        return res

