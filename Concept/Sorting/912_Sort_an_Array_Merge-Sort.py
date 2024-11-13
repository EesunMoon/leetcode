class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <=1:
            return nums
        mid = len(nums)//2
        left_side = self.sortArray(nums[:mid])
        right_side = self.sortArray(nums[mid:])
        return self.merge(left_side, right_side)
        
    def merge(self, left_nums, right_nums):
        left, right = 0, 0
        sorted_array = []
        while left < len(left_nums) and right < len(right_nums):
            if left_nums[left] <= right_nums[right]:
                sorted_array.append(left_nums[left])
                left += 1
            else:
                sorted_array.append(right_nums[right])
                right += 1
        
        # copying
        sorted_array.extend(left_nums[left:])
        sorted_array.extend(right_nums[right:])
        return sorted_array
