class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def heapify(heapsize, idx):
            largest = idx
            left = 2*idx+1
            right = 2*idx+2

            if left<heapsize and nums[left] > nums[largest]:
                largest = left
            if right <heapsize and nums[right] > nums[largest]:
                largest = right
            if largest != idx:
                nums[idx], nums[largest] = nums[largest], nums[idx]
                heapify(heapsize, largest)

        # build heap - top down
        n = len(nums)
        for i in range(n//2-1, -1, -1):
            heapify(n, i)
        
        for i in range(n-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)

        return nums