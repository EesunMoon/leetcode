class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. make hashmap (num:[idx]) T O(n) S O(n)
        count = defaultdict(list)
        for i, n in enumerate(nums):
            count[n].append(i)
        
        # 2. get index T O(kn)
        for i, n in enumerate(nums):
            find = target - n
            if not find in count:
                continue
            for idx in count[find]:
                if idx != i:
                    return [i, idx]