class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4,5] k=2, [4,5,1,2,3]
        # idx = (idx+k) % len(nums)
        # BF: T O(n*k) S O(1)
        # k~N-1 | 0~N-k: T O(n) S O(n)
        # [4,5,| 1,2,3]
        # reverse 1) [5,4,| 3,2,1]
        
        N = len(nums)
        k%=N
        def reverse(l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1; r -= 1
        
        # 1) reverse all -> [765|4321]
        reverse(0, N-1)
        # 2) re-reverse 0~k-1 and k~N-1 seperately
        reverse(0,k-1) # 5674321
        reverse(k, N-1) # 5671234