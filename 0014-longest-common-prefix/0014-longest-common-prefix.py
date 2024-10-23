class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # all same
        if len(set(strs)) == 1:
            return strs[0]
        
        # remove duplicates
        strs = list(set(strs))
        min_len = min(len(x) for x in strs)
        
        common = ""
        for x in zip(*strs):
            if len(set(x)) == 1:
                common += x[0]
            else:
                break
        
        return common
        