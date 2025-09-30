# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.to_load = collections.deque()

    def read(self, buf: List[str], n: int) -> int:
        cnt = 0
        buf4 = ['']*4

        while cnt < n:
            if not self.to_load:
                k = read4(buf4)
                if k == 0: # EOF
                    break
                self.to_load.extend(buf4[:k])
            
            buf[cnt] = self.to_load.popleft()
            cnt += 1
        return cnt
        