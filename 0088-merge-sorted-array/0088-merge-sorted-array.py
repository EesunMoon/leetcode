class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        i1, i2 = m-1, n-1

        for p in range(n+m-1, -1, -1):
            if i2 < 0:
                break
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[p] = nums1[i1]
                i1-=1
            else:
                nums1[p] = nums2[i2]
                i2 -= 1
    

        return nums1