# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.to_load = collections.deque()

    def read(self, buf: List[str], n: int) -> int:
        cnt = 0
        buf4 = ['']*4

        while cnt < n:
            if len(self.to_load) == 0:
                for i in range(read4(buf4)):
                    self.to_load.append(buf4[i])
                if len(self.to_load) == 0:
                    break
            else:
                buf[cnt] = self.to_load.popleft()
                cnt += 1
        return cnt
        