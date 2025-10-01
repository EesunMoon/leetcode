class Solution:
    def isPalindrome(self, s: str) -> bool:
        # alphanumeric: isalnum
        l, r = 0, len(s)-1
        
        while l<=r:
            if not s[l].isalnum() and not s[r].isalnum():
                l+=1; r-=1; continue
            if not s[l].isalnum():
                l += 1; continue
            if not s[r].isalnum():
                r -= 1; continue
            if s[l].lower()!=s[r].lower():
                return False
            l+=1; r-=1
        return True