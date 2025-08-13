class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. ignore non-alphanumeric => using ord
        # 2. same or not => two pointer O(n/2) -> T O(n), S O(1)

        def isAlphanumeric(w):
            return ((ord("a")<= ord(w)<=ord("z")) or
                    (ord("A")<= ord(w)<=ord("Z")) or
                    (ord("0")<= ord(w)<=ord("9")))
        l, r = 0, len(s)-1
        while l < r:
            if not isAlphanumeric(s[l]) and l < r:
                l += 1
                continue
            if not isAlphanumeric(s[r]) and l < r:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
