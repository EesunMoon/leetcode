class HitCounter:
    # past 300 seconds
    # 1, 3, 5, 400, 400, 401
    # 1, 2, 3, 300 << queue(deque)
    # get: 4 ->> 3
    # get: 300 (0~300) ->> 4
    # get: 301 (0~301) ->> 3
    # 200
    # rid = 2
    # [1, 3, 5, 300, 302, 401]
    #  l.    m   r           r        
    # gethit 300:: 0 --> -1 (return len)
    # gethit 303:: 3 --> 1. (return len-(1+1))
    # gethit 401:: 101 --> 

    def __init__(self):
        self.count = 0
        # self.q = collections.deque()
        self.q = []
        
    def hit(self, timestamp: int) -> None:
        # append timestamp into the deque , count the total counts --> T O(1)
        self.q.append(timestamp)
        self.count += 1
    
    def binarysearch(self, timestamp):
        l, r = 0, self.count-1
        target = timestamp-300
        rid = -1
        while l<=r:
            m = l + (r-l)//2
            if self.q[m] > target:
                r = m - 1
            else:
                rid = m
                l = m + 1
        return rid

    def getHits(self, timestamp: int) -> int:
        # remove the elements in deque, which is out out the bound (q[0] < timestamp-300)
        # while self.q and self.q[0] <= (timestamp-300):
        #     self.q.popleft()
        #     self.count -= 1
        return self.count - (self.binarysearch(timestamp)+1)
       


        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)