class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sorting T O(nlogn) S O(1)
        # hashset T O(n) S O(n)
        return len(set(nums)) != len(nums)