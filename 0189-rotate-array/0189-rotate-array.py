class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1, 2, 3, 4, | 5, 6, 7, k = 3
        5, 6, 7, | 1, 2, 3, 4 

        7, 6, 5, | 4, 3, 2, 1

        k = 2
        """
        n = len(nums)
        k = k % n
        
        def reverseList(l, r):
            while l<=r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # 1) reverse entire array (if splitting k, we can make like moving )
        reverseList(0, n-1)

        # 2) left portion(split up to k-1th) - reverse again
        reverseList(0, k-1)

        # 3) right portion - reverse again
        reverseList(k, n-1)