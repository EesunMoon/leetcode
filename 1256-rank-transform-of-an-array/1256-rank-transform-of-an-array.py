class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(set(arr))
        num_to_rank = {num: rank + 1 for rank, num in enumerate(sorted_arr)}
        return [num_to_rank[num] for num in arr]
        