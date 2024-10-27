class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        s = s.lower() # convert to lower
        new_s =""
        for x in s:
            if x.isalnum():
                new_s += x
        
        i, j = 0, len(new_s)-1
        while i< j:
            if new_s[i] != new_s[j]:
                return False
            else:
                i+=1
                j-=1

        return True