class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        l, h = 0, len(self.prefix)
        while l < h:
            m = l + (h-l)//2
            if target > self.prefix[m]:
                l = m + 1
            else:
                h = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()