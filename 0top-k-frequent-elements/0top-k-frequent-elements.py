class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count=Counter(nums) # keys: count_num, values: nums
 
        return heapq.nlargest(k, count.keys(), key=count.get)