class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1
        count = 1
        
        while start < len(nums):
            if nums[start] == nums[start-1]:
                count += 1
                if count > 2:
                    nums.pop(start)
                    start-= 1
                    count -= 1
            else:
                count = 1
            start +=1
        return len(nums)
        """
        for j in range(total):
            if nums[j] != nums[start]:
                count = j - start
                if count > 2:
                    # nums = nums[0:start+2] + nums[j:] + nums[start+2:start+count]
                    nums[start+2:] = nums[j:] + nums[start+2:start+count]
                    total -= (count-2)
                    start += j
                    print(total, count)
                else:
                    start += count
                count = 0
        
        
        print(total)
        nums = nums[:total]
        return total
        """
        
        
        