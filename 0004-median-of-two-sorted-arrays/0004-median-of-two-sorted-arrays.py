class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # consider the size of A is smaller than that of B
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)-1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            Aleft = A[i] if i>=0 else float("-INF")
            Aright = A[i+1] if i+1 < len(A) else float("INF")
            Bleft = B[j] if j>=0 else float("-INF")
            Bright = B[j+1] if j+1 < len(B) else float("INF")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)+min(Aright,Bright))/2.0
            elif Aleft > Bright:
                # reduce the size of A
                r = i-1
            else:
                # increase the size of A
                l = i+1