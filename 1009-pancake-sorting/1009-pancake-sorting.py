class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []

        def reverse(k): # O(k), O(1)
            l, r = 0, k-1
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1; r -= 1
        
        def getMaxIdx(i): # O(k), O(1)
            maxIdx = 0; maxNum = arr[0]
            for idx in range(1, i+1):
                if maxNum < arr[idx]:
                    maxIdx, maxNum = idx, arr[idx]
            return maxIdx
        
        for i in range(len(arr)-1, -1, -1):
            targetIdx = getMaxIdx(i) # O(k)
                
            if targetIdx != i:
                if targetIdx != 0:
                    reverse(targetIdx+1) # O(k)
                    res.append(targetIdx+1)
                reverse(i+1)
                res.append(i+1)

        return res #O(n*k)
            


        
