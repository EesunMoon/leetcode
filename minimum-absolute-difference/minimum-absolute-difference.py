class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        arr.sort()
        min_diff = float("inf")

        answer = []
        for i in range(len(arr)-1):
            curr_diff = arr[i+1]- arr[i]
            if curr_diff == min_diff:
                answer.append([arr[i], arr[i+1]])
            elif curr_diff < min_diff:
                min_diff = curr_diff
                answer = [[arr[i], arr[i+1]]]
        
        return answer