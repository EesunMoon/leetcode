class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def Pow(i):
            if i == 0:
                return 1
            if i == 1:
                return x
            
            mid = Pow(i//2)
            if i % 2:
                return mid * mid * x
            else:
                return mid * mid
        
        return Pow(n) if n > 0 else 1/Pow(abs(n))