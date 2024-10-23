class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack or not needle:
            return -1
        
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)