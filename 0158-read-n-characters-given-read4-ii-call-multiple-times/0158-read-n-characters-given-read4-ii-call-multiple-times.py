# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

# abcd | efgh | ijkl | mnop,  n = 3, n = 2, n=5
# abc d => buf: abc
# read4, fqhi: defgh
# storage: deque
# 1. cnt = 0 
#### iter: if not storage -> read4 and then store
## storage: kl < O(7)
## buf = [fghij] cnt = 3

class Solution:
    def __init__(self):
        self.storage = collections.deque()
    def read(self, buf: List[str], n: int) -> int:
        cnt = 0

        while cnt < n:
            if not self.storage:
                buf4 = [""]*4
                if read4(buf4):
                    for v in buf4:
                        self.storage.append(v)
                else:
                    break
            else:
                buf[cnt] = self.storage.popleft()
                cnt += 1

        return cnt

        