class StockSpanner:

    def __init__(self):
        # monotonic stack
        self.stack = [] # [price, cnt]

    def next(self, price: int) -> int:
        # equal or less - monotonic stack
        cnt = 1 # contain itself
        while self.stack and self.stack[-1][0] <= price:
            cnt += self.stack.pop()[1]
        self.stack.append([price, cnt])
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)