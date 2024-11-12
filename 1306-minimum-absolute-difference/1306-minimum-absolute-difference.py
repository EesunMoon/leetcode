class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        min_element = min(arr)
        max_element = max(arr)
        count = [0] * (max_element - min_element + 1)

        for ele in arr:
            count[ele-min_element] += 1
        
        prev = 0
        min_diff = max_element - min_element
        answer = []
        for curr in range(1, len(count)):
            if count[curr] == 0:
                continue
            if curr- prev == min_diff:
                answer.append([prev+min_element, curr+min_element])
            elif curr-prev < min_diff:
                min_diff = curr- prev
                answer = [[prev+min_element, curr+min_element]]
        
            prev = curr
        return answer