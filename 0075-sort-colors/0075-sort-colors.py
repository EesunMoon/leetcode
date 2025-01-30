class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        print(hashmap)
        idx = 0
        for i in range(3): # color
            if i not in hashmap:
                continue
            while hashmap[i] != 0:
                nums[idx] = i
                hashmap[i] -= 1
                idx += 1
        return nums
        