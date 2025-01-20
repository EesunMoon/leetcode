class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        maxDist = 0
        minVal, maxVal = arrays[0][0], arrays[0][-1]
        
        for i in range(1, len(arrays)):
            arr = arrays[i]
            maxDist = max(maxDist, abs(arr[-1]-minVal), abs(arr[0]-maxVal))
            minVal, maxVal = min(minVal, arr[0]), max(maxVal, arr[-1])
        
        return maxDist