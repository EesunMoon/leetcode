class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotate = {'2', '5', '6', '9'} # must contain
        invalid = {'3', '4', '7'} # must not contain
        
        def is_good(num):
            digits = set(str(num))
            if digits & invalid:
                return False
            return bool(digits & rotate)
                        
        cnt = 0
        for i in range(1, n+1):
            if is_good(i):
                cnt += 1
        return cnt
