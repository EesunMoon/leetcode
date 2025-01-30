class Solution:
    def reverse(self, x: int) -> int:
        res = 0 
        flag = True if x > 0 else False
        boundary = 2**31
        x = abs(x)
        while x:
            res = res * 10 + (x % 10)
            x //= 10
            if res > boundary:
                return 0
            
        if (flag and res > boundary) or (flag == False and res <= -boundary):
            return 0
            
        return res if flag else -res
