class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        min_element = min(arr)
        max_element = max(arr)
        shift = -min_element

        counts = [0] * (max_element - min_element +1)
        answer = []

        for e in arr:
            counts[e+shift] += 1

        min_pair_diff = max_element - min_element
        prev = 0

        for curr in range(1, max_element+shift +1):
            if counts[curr] == 0:
                continue
            if curr - prev == min_pair_diff:
                answer.append([prev-shift, curr-shift])
            elif curr-prev < min_pair_diff:
                answer = [[prev-shift, curr-shift]]
                min_pair_diff = curr-prev
            prev = curr
        return answer