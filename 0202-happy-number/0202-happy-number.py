class Solution:
    def isHappy(self, n: int) -> bool:
        
        def help(n):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = help(n)
        return n == 1