class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minNum = min(nums)
        minNum = abs(min(minNum, 0))
        maxNum = max(nums) + minNum
        count = [0] * (maxNum+1)

        for num in nums:
            count[num+minNum] += 1
        
        idx = maxNum
        while k > 0:
            k -= count[idx]
            idx -= 1
        
        return idx+1-minNum