class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using hashmap T O(n) S O(n)
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
        """

        # using pointer
        l, r = 0, len(nums)-1 # red, blue

        curr = 0
        while curr <= r:
            if nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                l += 1
            elif nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
                curr -= 1 # check this position once more
            curr += 1