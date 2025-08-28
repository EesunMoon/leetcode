class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # assign small length's array as A
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        # binary search using A (smaller length's array)
        l, r = 0, len(A)-1
        while True:
            i = (l+r) // 2 # A
            j = half - i - 2 # B (consider index starting from 0)

            Aleft = A[i] if i>=0 else float("-inf") # edge case: if array is not existed
            Aright = A[i+1] if (i+1) < len(A) else float("inf") # edge case: i+1 is out of bound
            Bleft = B[j] if j>=0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # case1) odd
                if total % 2: 
                    return min(Aright, Bright)
                # case 2) even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            # too many elements in A
            elif Aleft > Bright: 
                r = i - 1
            # not enough elements in A
            else: 
                l = i + 1