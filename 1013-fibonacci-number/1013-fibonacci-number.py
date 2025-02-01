class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n == 0:
            return 0
        if n == 1:
            return 1

        one = 0
        two = 1

        for _ in range(n-1):
            tmp = one+two
            one = two
            two = tmp
        return two