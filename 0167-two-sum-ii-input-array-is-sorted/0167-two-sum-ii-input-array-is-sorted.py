class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # BF - all combination: T O(n^2) S O(1)
        # binary search - T (nlogn)
        # two pointer using combination - T O(n)

        l, r = 0, len(numbers)-1
        while l<r:
            comb = numbers[l] + numbers[r]
            if comb == target:
                return [l+1, r+1]
            elif comb < target:
                l += 1
            else:
                r -= 1