class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        """
        def returnPrefix(str1, str2):
            if len(str2) > len(str1):
                str1, str2 = str2, str1
            
            res = ""
            i1, i2 = 0, 0
            while i1 < len(str1):
                while i1<len(str1) and i2<len(str2) and str1[i1] == str2[i2]:
                    res += str1[i1]
                    i1 += 1
                    i2 += 1
                break
            return res
        
        for i in range(len(strs)-1):
            prefix = returnPrefix(strs[i], strs[i+1])
            if prefix == "":
                return ""
            strs[i+1] = prefix
        return strs[len(strs)-1]
        """
        def isCommonPrefix(l):
            str1 = strs[0][:l]
            for i in range(1, len(strs)):
                if not strs[i].startswith(str1):
                    return False
            return True

        minLen = min(len(x) for x in strs)
        low, high = 1, minLen
        while low <= high:
            middle = (low + high) // 2
            if isCommonPrefix(middle):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][:(low+high)//2]