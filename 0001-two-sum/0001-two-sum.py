class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make hashmap (num : [index]) -> T O(n)
        hashmap = collections.defaultdict(list)
        for i, num in enumerate(nums):
            hashmap[num].append(i)
        
        # find index
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in hashmap:
                continue
            for idx in hashmap[diff]:
                if idx != i:
                    return [i, idx]