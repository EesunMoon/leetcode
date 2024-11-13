class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]] - place, index
        :rtype: List[int]
        """
        answer = []
        for k, idx in queries:
            target = [(int(num[-idx:]), i) for i, num in enumerate(nums)]
            
            target.sort()
            answer.append(target[k-1][1])
        return answer