class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.stream = nums
        self.stream.sort()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        idx = self.getIndex(val)
        self.stream.insert(idx, val)
        return self.stream[-self.k]
        
        return self.min_heap[0]
    
    def getIndex(self, val):
        left, right = 0, len(self.stream)-1

        while left <= right:
            mid = (left+right)//2
            mid_ele = self.stream[mid]
            
            if mid_ele == val:
                return mid
            elif mid_ele > val:
                right = mid-1
            else:
                left = mid+1

        return left
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
