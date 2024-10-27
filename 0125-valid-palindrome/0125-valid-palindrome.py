class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # .isalnum() : check alphabetic
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]
        
        return filtered_chars_list == reversed_chars_list

        """
        Approach 1)
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
        """