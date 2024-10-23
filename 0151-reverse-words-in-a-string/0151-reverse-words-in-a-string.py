class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        s_list.reverse()
        
        return " ".join(s_list)
        